import os 
import requests
import uuid

def set_multiline_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        delimiter = uuid.uuid1()
        print(f'{name}<<{delimiter}', file=fh)
        print(value, file=fh)
        print(delimiter, file=fh)

name = 'template'
value = "### INFO on your PR" + uuid.uuid1()

try:
    PR_NUMBER = os.environ["PR_NUMBER"]
except KeyError:
    PR_NUMBER = "Pr number Token not available!"

try:
    GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
except KeyError:
    GITHUB_TOKEN = "GitHub Token not available!"

apiCall = "https://api.github.com/repos/HyperCollect/datasets/pulls/" + str(PR_NUMBER) + "/files"

headers = {'Authorization': 'token ' + GITHUB_TOKEN}

response = requests.get(apiCall, headers=headers)
res = response.json()

if len(res) > 0:
    for file in res:
        value = value + file['filename'] + "\n"
else:
    print("Response is empty!")

set_multiline_output("template", value)
