# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
"""correcting the attribute name in the class definition"""
class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value    
        self.limit = limit

r = Record("R-001", 87.0, 100.0)
print(r.value)

#AttributeError: 'Record' object has no attribute 'value
#fixed it by correcting .amount to .value