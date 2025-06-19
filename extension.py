from typing import Optional

def extension_hook(hook_name, context) -> Optional[dict]:
    # Perform any necessary setup
    if hook_name == 'beforeAll':
        print(f"Setting up test suite: {context['suite'].get('description', '')}")

        # Add an additional test case to the suite:
        context["suite"]["tests"].append(
            {
                "vars": {
                    "body": "It's a beautiful day",
                    "language": "Spanish",
                },
                "assert": [{"type": "contains", "value": "Es un día hermoso."}],
            }
        )

        # Add an additional default assertion to the suite:
        context["suite"]["defaultTest"]["assert"].append({"type": "is-json"})

        return context

    # Perform any necessary teardown or reporting
    elif hook_name == 'afterAll':
        print(f"Test suite completed: {context['suite'].get('description', '')}")
        print(f"Total tests: {len(context['results'])}")

    # Prepare for individual test
    elif hook_name == 'beforeEach':
        print(f"Running test: {context['test'].get('description', '')}")

        # Change all languages to pirate-dialect
        context["test"]["vars"]["language"] = f'Pirate {context["test"]["vars"]["language"]}'

        return context

    # Clean up after individual test or log results
    elif hook_name == 'afterEach':
        print(f"Test completed: {context['test'].get('description', '')}. Pass: {context['result'].get('success', False)}")

