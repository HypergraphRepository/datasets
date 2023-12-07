import os

try:
    PR_NUMBER = os.environ["PR_NUMBER"]
except KeyError:
    PR_NUMBER = "Token not available!"

print(f"PR_NUMBER: {PR_NUMBER}")