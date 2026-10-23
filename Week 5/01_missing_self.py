# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
"""adding the missing 'self' in method"""
class Record:
    def status(self,percent):    # this parameter should be self
        return percent

r = Record()
print(r.status(95))
#TypeError: Record.status() takes 1 positional argument but 2 were given
#fixed it by adding self in (self,percent)