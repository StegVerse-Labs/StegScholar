#!/usr/bin/env python3
"""Deterministic tests for the scalar delayed-control benchmark.

The tests use only the Python standard library and intentionally verify mechanics
and labels rather than claiming empirical support for the Rigel number.
"""

from __future__ import annotations

import importlib.util
import math
import random
import sys
import unittest
from collections import deque
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("scalar_delayed_control.py")
SPEC = importlib.util.spec_from_file_location("scalar_delayed_control", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load benchmark module from {MODULE_PATH}")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class DelayMechanicsTests(unittest.TestCase):
    def test_delay_steps_rounds_to_nearest_step(self) -> None:
        self.assertEqual(MODULE.delay_steps(0.00, 0.01), 0)
        self.assertEqual(MODULE.delay_steps(0.024, 0.01), 2)
        self.assertEqual(MODULE.delay_steps(0.026, 0.01), 3)

    def test_delayed_value_zero_delay_returns_current_value(self) -> None:
        queue: deque[float] = deque()
        self.assertEqual(MODULE.delayed_value(queue, 1.5, 0), 1.5)
        self.assertEqual(MODULE.delayed_value(queue, 2.5, 0), 2.5)

    def test_delayed_value_preserves_requested_lag(self) -> None:
        queue: deque[float] = deque()
        outputs = [MODULE.delayed_value(queue, value, 2) for value in (1.0, 2.0, 3.0, 4.0)]
        self.assertEqual(outputs, [1.0, 2.0, 1.0, 2.0])


class RigelScoreTests(unittest.TestCase):
    def test_rigel_number_has_expected_algebra(self) -> None:
        value = MODULE.rigel_number(
            lam=4.0,
            alpha=0.25,
            V=0.20,
            delta_0=0.01,
            kappa=1.0,
            floor=1e-9,
        )
        self.assertAlmostEqual(value, 1.0 / math.log(20.0), places=12)

    def test_rigel_number_increases_with_total_latency(self) -> None:
        common = dict(lam=2.0, V=1.0, delta_0=0.1, kappa=1.0, floor=1e-9)
        low = MODULE.rigel_number(alpha=0.1, **common)
        high = MODULE.rigel_number(alpha=0.2, **common)
        self.assertGreater(high, low)

    def test_rigel_number_is_infinite_without_positive_margin_ratio(self) -> None:
        value = MODULE.rigel_number(1.0, 0.1, 0.1, 0.1, 1.0, 1e-9)
        self.assertTrue(math.isinf(value))


class SamplingAndPartitionTests(unittest.TestCase):
    def test_split_assignment_is_deterministic(self) -> None:
        expected = ["ood", "train", "train", "train", "train", "ood"]
        actual = [MODULE.split_for_episode(index) for index in range(6)]
        self.assertEqual(actual, expected)

    def test_total_latency_equals_phase_sum(self) -> None:
        cfg = MODULE.Config(episodes=100)
        episode = MODULE.run_episode(1, cfg, random.Random(1234))
        self.assertAlmostEqual(
            episode.alpha_total,
            episode.alpha_o + episode.alpha_i + episode.alpha_r,
            places=15,
        )
        self.assertAlmostEqual(episode.burden_o, episode.lambda_growth * episode.alpha_o, places=15)
        self.assertAlmostEqual(episode.burden_i, episode.lambda_growth * episode.alpha_i, places=15)
        self.assertAlmostEqual(episode.burden_r, episode.lambda_growth * episode.alpha_r, places=15)

    def test_episode_replay_is_stable_for_fixed_seed(self) -> None:
        cfg = MODULE.Config(episodes=100)
        first = MODULE.run_episode(7, cfg, random.Random(98765))
        second = MODULE.run_episode(7, cfg, random.Random(98765))
        self.assertEqual(first, second)


class OutcomeLabelTests(unittest.TestCase):
    def test_recovered_label_implies_no_safety_violation_and_target_return(self) -> None:
        cfg = MODULE.Config(episodes=100)
        episode = MODULE.run_episode(3, cfg, random.Random(42))
        if episode.recovered:
            self.assertEqual(episode.safety_violated, 0)
            self.assertLessEqual(episode.terminal_mean_abs_x, cfg.target_abs_x)

    def test_safety_violation_prevents_recovery(self) -> None:
        cfg = MODULE.Config(
            episodes=100,
            safety_abs_x=0.05,
            initial_abs_x=(0.20, 0.20),
            process_noise_sd=(0.0, 0.0),
            sensor_noise_sd=(0.0, 0.0),
        )
        episode = MODULE.run_episode(1, cfg, random.Random(9))
        self.assertEqual(episode.safety_violated, 1)
        self.assertEqual(episode.recovered, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
