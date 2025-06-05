import os 
import requests
import uuid
import fastjsonschema
import json

def set_multiline_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        delimiter = uuid.uuid1()
        print(f'{name}<<{delimiter}', file=fh)
        print(value, file=fh)
        print(delimiter, file=fh)

def hif_file_is_ok(rawApiCall):
    url = "https://raw.githubusercontent.com/pszufe/HIF-standard/main/schemas/hif_schema.json"
    schema = requests.get(url).json()
    validator = fastjsonschema.compile(schema)
    rawResponse = requests.get(rawApiCall)
    # rawRes = rawResponse.text
    hiftext = json.load(rawResponse)
    try:
        validator(hiftext)
        print("HIF-Compliant JSON.")
        return True
    except Exception as e:
        print(f"Invalid JSON: {e}")
        return False

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

def hgf_file_is_ok(rawApiCall):
    rawResponse = requests.get(rawApiCall)
    rawRes = rawResponse.text
    # check that file format is correct like:
    # 16 4
    # 1=true 2=true 3=true
    # 4=true 5=true 6=true
    firstLine = rawRes.splitlines()[0]
    splitFirstLine = firstLine.split(" ")
    if len(splitFirstLine) != 2:
        return False
    if not splitFirstLine[0].isdigit() or not splitFirstLine[1].isdigit():
        return False

    for line in rawRes.splitlines()[1:]:
        if line == "":
            continue
        for element in line.split(" "):
            if element == "" or element == "\n":
                continue
            splitElement = element.split("=")
            if len(splitElement) != 2:
                return False
            if not splitElement[0].isdigit():
                return False
            if splitElement[1] == "":
                return False
        
    return True

def categories_is_ok(rawApiCall):
    rawResponse = requests.get(rawApiCall)
    rawRes = rawResponse.text
    # check that file format is correct like:
    # domain
    # ---
    # category1
    # category2
    # category3
    txt = rawRes.splitlines()
    category = txt[0]
    types = []
    if category == "":
        return False
    if rawRes.splitlines()[1] != "---":
        return False
    else:
        for line in rawRes.splitlines()[2:]:
            if line == "":
                continue
            types.append(line)
        if len(types) == 0:
            return False
    return True

name = 'template'
value = f'### INFO on your PR\n'

commentid = uuid.uuid1()
with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
    print(f'commentid={commentid}', file=fh)
iserror = False

try:
    PR_NUMBER = os.environ["PR_NUMBER"]
except KeyError:
    PR_NUMBER = "Pr number Token not available!"

try:
    GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
except KeyError:
    GITHUB_TOKEN = "GitHub Token not available!"

baseline = "https://api.github.com/repos/HypergraphRepository/datasets"
pr_files_get = baseline + "/pulls/" + str(PR_NUMBER) + "/files"
pr_add_label_post = baseline + "/issues/" + str(PR_NUMBER) + "/labels"

headers = {'Authorization': 'token ' + GITHUB_TOKEN}

response = requests.get(pr_files_get, headers=headers)
res = response.json()

if len(res) > 0:
    # check if files are just modified
    all_added = True
    for file in res:
        if file['status'] != "added":
            all_added = False
            break

    if not all_added:
        value = value + "Not all files are new!\nAdding a reviewer to check the changes\n"
        requests.post(pr_add_label_post, headers=headers, data='{"labels":["enhancement"]}')
    else:
        # Only new files are in the pull request
        # check if the mandatory files are in the pull request
        requests.post(pr_add_label_post, headers=headers, data='{"labels":["hgcreation"]}')
        mdFile = False
        infoFile = False
        hgFile = False
        hifFile = False

        for file in res:
            if file['filename'].endswith(".md"):
                mdFile = True
            if file['filename'].endswith(".info"):
                infoFile = True
            if file['filename'].endswith(".hgf"):
                hgFile = True
            if file['filename'].endswith(".hif"):
                hifFile = True

        # check the format of the files
        for file in res:
            if file['filename'].endswith(".md"):
                value = value + "- [x] " + file['filename'] + "\n"
            elif file['filename'].endswith(".info"):
                # check format of categories file
                if categories_is_ok(file['raw_url']):
                    value = value + "- [x] " + file['filename'] + "\n"
                else:
                    value = value + "- [ ] " + file['filename'] + " is not in correct format\n"
            elif file['filename'].endswith(".hgf"):
                # check format of hypergraph file
                if hgf_file_is_ok(file['raw_url']):
                    value = value + "- [x] " + file['filename'] + "\n"
                else:
                    value = value + "- [ ] " + file['filename'] + " is not in correct format\n"
            elif file['filename'].endswith(".hif"):
                # check format of HIF format https://github.com/pszufe/HIF-standard
                if hif_file_is_ok(file['raw_url']):
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
            value = value + "- [ ] No hgf file found!\n"
        if not hifFile:
            value = value + "- [ ] No hif file found!\n"
        if not mdFile or not infoFile or not hgFile:
            requests.post(pr_add_label_post, headers=headers, data='{"labels":["missing file"]}')
            iserror = True        
else:
    value = value + "Response is empty!"
    exit(1)

set_multiline_output("template", value)

with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
    print(f'iserror={iserror}', file=fh)