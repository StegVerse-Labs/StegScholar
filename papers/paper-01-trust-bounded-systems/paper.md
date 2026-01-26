# Trust-Bounded Socio-Technical Systems: Architectural Primitives for Auditability and Failure

## Abstract
Distributed systems increasingly combine human actors, automated components, and institutional processes, yet commonly treat trust as an implicit assumption rather than an explicit system property...

## 1. Introduction
Modern systems rarely operate in purely technical domains...

## 2. Contributions
1. Trust as mutable system state  
2. Irrecoverable audit loss as operational state  
3. Boundary enforcement as mechanism  
4. Survivability under epistemic constraint  

## 3. Trust as State
Trust persists, decays, and may become phantom...

## 4. Boundary Enforcement
Boundaries constrain action independent of intent...

## 5. Auditability and Irrecoverable Audit Loss
Audit loss may occur even when logging works as designed...

## 6. Minimal Model
Trust ∈ {high, degraded, unknown}  
Boundary ∈ {enabled, restricted, revoked}  
Audit ∈ {available, partial, irrecoverable}

## 7. Vignette
A distributed system loses historical logs due to policy change...

## 8. Related Work
Distributed systems assume bounded observability...

## 9. Limitations
This framework bounds behavior, not correctness.
