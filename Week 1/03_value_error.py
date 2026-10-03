# BROKEN ON PURPOSE.
# Run it, type 23.7 when asked, read the last line, then fix it.

value = float(input("Value: "))

print(value)
#ValueError: invalid literal for int() with base 10: '23.7'
#changed int to float to fix error