import json

def create_tests():
    test_cases = []

    # Load test data from database, API, etc.
    test_data = load_test_data()

    for item in test_data:
        test_cases.append({
            "vars": {
                "input": item["input"],
                "context": item["context"]
            },
            "assert": [{
                "type": "contains",
                "value": item["expected"]
            }]
        })

    return test_cases

    