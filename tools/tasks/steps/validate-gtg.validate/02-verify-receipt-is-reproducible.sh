cp receipts/gtg/fixture-validation-receipt.json /tmp/first.json
python scripts/validate_gtg_fixtures.py
cmp /tmp/first.json receipts/gtg/fixture-validation-receipt.json
