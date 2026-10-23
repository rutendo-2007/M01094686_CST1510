# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
"""adding an object to a method"""
class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        return "OVER LIMIT" if self.value > self.limit else "OK"

r = Record("R-001", 120.0, 100.0)
print(r.status())
#NameError: name 'status' is not defined
#fixed it by adding the object 'r' so its r.status