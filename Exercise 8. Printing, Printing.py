formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 5))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))

print(formatter.format(
     "Try your",
     "Own test here",
     "M",
     "Or"
))
