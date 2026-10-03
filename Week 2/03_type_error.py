# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

limit = 20
value = int(input("Value: "))

if value > limit:
    print("OVER")
else:
    print("OK")
#TypeError: '>' not supported between instances of 'str' and 'int'
#fixed error by wrapping input command with int()