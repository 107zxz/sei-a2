import sys
import json
import requests
import argparse
import difflib

# flask run -p 3000
greetings_base = "http://127.0.0.1:3000/"
timestamp_base = "http://127.0.0.1:3001/"
dice_roll_base = "http://127.0.0.1:3002/"
input_validate_base = "http://127.0.0.1:3004/"
calculate_base = "http://127.0.0.1:3005/"
format_output_base = "http://127.0.0.1:3006/"

def compare_contents(response, expected_string):

    # If contents are the same, return 0
    if response.decode('utf-8').splitlines() == expected_string.splitlines():
        return 0
    
    # Else, determine differences between response and expected
    else:
        d = difflib.Differ()
        diff = list(d.compare(response.decode('utf-8').splitlines(), expected_string.splitlines()))

        return ('\n'.join(diff))

def test_microservice(test):

    base_url='http://kube.info'
    bypass_url = ''
    expected_string = ''

    # Get expected output from files as they're quite long...
    with open('expected_greetings.txt', 'rb') as file:
        expected_greetings = file.read().decode('utf-8')

    with open('expected_internal_error.txt', 'rb') as file:
        expected_internal_error = file.read().decode('utf-8')

    # Define url and expected outputs
    if test['endpoint'] == "noncomm/greetings":
        bypass_url = greetings_base

        expected_string = expected_greetings

    elif test['endpoint'] == "noncomm/timestamp":
        bypass_url = timestamp_base
        expected_string = '<p>The current date and time is: <b>2023-10-31 23:59:59</b>.</p>'

    elif test['endpoint'] == "noncomm/dice_roll":
        bypass_url = dice_roll_base
        expected_string = '<p>You rolled a <b>6</b>.</p>'

    elif test['endpoint'] == "comm/increment": # input_validate
        bypass_url = input_validate_base

        if test['parameters']:
            try:
                integer = int(test['parameters']['input'])

                # Internal error is expected when running in bypass mode,
                # due to being disconnected to next microservice 
                if args.bypass:
                    expected_string = expected_internal_error
                else:
                    expected_string = f"<p>Your result is: <b>{integer + 1}</b>.</p>"

            except ValueError:
                expected_string = "<p>Invalid input</p>"
        else:
            expected_string = "<p>Invalid input</p>"

    elif test['endpoint'] == "comm/inc-calculate":
        bypass_url = calculate_base

        if test['parameters']:
            try:
                integer = int(test['parameters']['input'])
                expected_string = f"{integer + 1}"

            # Internal error expected if input isn't integer, 
            # as only input_validate will prevent this
            except ValueError:
                expected_string = expected_internal_error
        else:
            expected_string = expected_internal_error

    elif test['endpoint'] == "comm/inc-format-output":
        bypass_url = format_output_base

        if test['parameters']:
            expected_string = f"<p>Your result is: <b>{test['parameters']['input']}</b>.</p>"
        else:
            expected_string = "<p>Invalid input</p>"

    # Define URL if in bypass mode
    if args.bypass:
        url = bypass_url
    else:
        url = f'{base_url}/{test["endpoint"]}'

    print(f"\nTesting {test['endpoint']}:")
    print(f"Requesting: {url} with parameters: {test['parameters']}")

    # Try requesting URL endpoint
    try:
        response = requests.get(url, params=test['parameters'])

        # print("Status code:", response.status_code)
        # print("\nResponse body:", response.content)
        # print("\nExpected body:", expected)

        comparison = compare_contents(response.content, expected_string)

        if comparison:
            print("Output is different than expected, check differences:")
            print(comparison)
        else:
            print("Output is same as expected, test passed.")

    except Exception as e:
        print(e)

# Parse arguments
parser = argparse.ArgumentParser(description='Run test cases against existing microservices.')
parser.add_argument('--bypass', action='store_true', help='Bypass gateway and directly query microservices')
args = parser.parse_args()

# Load test data
with open('tests.json') as json_file:
    tests = json.load(json_file)

# Run tests
for test in tests:
    test_microservice(test)    

