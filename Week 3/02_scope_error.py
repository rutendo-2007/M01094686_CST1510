# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"
    return status

print(check(87, 100))


#NameError: name 'status' is not defined
#fixed error by adding 'return stutus' to the function definition and adding 'print' to the function call