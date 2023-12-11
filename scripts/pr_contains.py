import os 
import requests
import uuid

def set_multiline_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        delimiter = uuid.uuid1()
        print(f'{name}<<{delimiter}', file=fh)
        print(value, file=fh)
        print(delimiter, file=fh)

def hg_file_is_ok(rawApiCall):
    rawResponse = requests.get(rawApiCall)
    rawRes = rawResponse.text

    # check that each line is numbers separated by commas
    # e.g. 0,1
    #      2,3
    #      4,5,6
    for line in rawRes.splitlines():
        if line == "":
            return False
        for number in line.split(","):
            if number == "":
                continue
            if not number.isdigit():
                return False
    return True

name = 'template'
value = f'### INFO on your PR\n'

commentid = uuid.uuid1()
with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
    print(f'commentid={commentid}', file=fh)

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
    mdFile = False
    infoFile = False
    hgFile = False

    # check if all files are in the pull request
    for file in res:
        if file['filename'].endswith(".md"):
            mdFile = True
        if file['filename'].endswith(".info"):
            infoFile = True
        if file['filename'].endswith(".hg"):
            hgFile = True

    for file in res:
        if file['filename'].endswith(".md"):
            value = value + "- [x] " + file['filename'] + "\n"
        elif file['filename'].endswith(".info"):
            value = value + "- [x] " + file['filename'] + "\n"
        elif file['filename'].endswith(".hg"):
            # check format of hg file
            if hg_file_is_ok(file['raw_url']):
                value = value + "- [x] " + file['filename'] + "\n"
            else:
                value = value + "- [ ] " + file['filename'] + " is not in correct format\n"
        else:
            value = value + "- [x] additional file not request!\n"

    if not mdFile:
        value = value + "- [ ] No markdown file found!\n"
    if not infoFile:
        value = value + "- [ ] No info file found!\n"
    if not hgFile:
        value = value + "- [ ] No hg file found!\n"
    if not mdFile or not infoFile or not hgFile:
        set_multiline_output("template", value)
        exit(1)
else:
    value = value + "Response is empty!"
    set_multiline_output("template", value)
    exit(1)

set_multiline_output("template", value)
