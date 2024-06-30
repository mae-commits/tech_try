# import_test.py
try:
    from tfcausalimpact import CausalImpact

    print("tfcausalimpact is successfully imported.")
except ImportError as e:
    print(f"Error importing tfcausalimpact: {e}")
