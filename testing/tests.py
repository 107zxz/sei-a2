import sys
import json
import requests
import argparse
import difflib

# flask run -p 3000
greetings_base = "http://127.0.0.1:3000/"
timestamp_base = "http://127.0.0.1:3000/"
dice_roll_base = "http://127.0.0.1:3000/"
input_validate_base = "http://127.0.0.1:3000/"
calculate_base = "http://127.0.0.1:3000/"
format_output_base = "http://127.0.0.1:3000/"

# TODO: add output comparisons
def compare_contents(content1, content2):
    d = difflib.Differ()
    diff = list(d.compare(content1.decode('utf-8').splitlines(), content2.decode('utf-8').splitlines()))

    print('\n'.join(diff))

def test_microservice(test):

    base_url='http://kube.info'
    bypass_url = ''
    compare_file = ''

    if test['endpoint'] == "noncomm/greetings":
        bypass_url = greetings_base
        compare_file = 'expected_greetings.txt'

    elif test['endpoint'] == "noncomm/timestamp":
        bypass_url = timestamp_base
        compare_file = 'expected_timestamp.txt'

    elif test['endpoint'] == "noncomm/dice_roll":
        bypass_url = dice_roll_base
        compare_file = 'expected_dice_roll.txt'

    elif test['endpoint'] == "comm/increment": # input_validate
        bypass_url = input_validate_base

    elif test['endpoint'] == "comm/inc-calculate":
        bypass_url = calculate_base

    elif test['endpoint'] == "comm/inc-format-output":
        bypass_url = format_output_base

    if args.bypass:
        url = bypass_url
    else:
        url = f'{base_url}/{test["endpoint"]}'

    print(f"\nTesting {test['endpoint']}")
    print(f"Requesting: {url} with parameters: {test['parameters']}")

    # Try making a request to url endpoint
    try:
        response = requests.get(url, params=test['parameters'])
        print("Status code:", response.status_code)
        # print("Response body:", response.content)

        with open(compare_file, 'rb') as file:
            expected = file.read()

        # print("\nExpected body:", expected)

        compare_contents(response.content, expected)

    except Exception as e:
        print(e)

parser = argparse.ArgumentParser(description='Run test cases against existing microservices.')
parser.add_argument('--bypass', action='store_true', help='Bypass gateway and directly query microservices')
args = parser.parse_args()

diff = difflib.Differ()

# Load test data from the JSON file
with open('tests.json') as json_file:
    tests = json.load(json_file)

# Run tests
base = ""
for test in tests:
    test_microservice(test)    

