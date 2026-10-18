# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
"""searching for file folder"""

with open("Week 04 - Lists, Dictionaries and Files\\LAB\\records_sample.txt") as f:
    print(f.read())
#FileNotFoundError: [Errno 2] No such file or directory: 'records.txt' as its not found in warmup folder
#replaced with relative path of records_sample.txt thats available in the LAB folder