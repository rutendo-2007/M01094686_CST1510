# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
"""deleting a key that is non existent"""

record = {"label": "R-001", "value": 87.0, "limit": 100.0}

print(record["value"])
#KeyError: 'status as its not in the record dictionary
#removed status and replaced with value
