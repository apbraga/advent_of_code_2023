import re

t = 0

n = "one two three four five six seven eight nine".split()

p = "(?=(" + "|".join(n) + "|\\d))"


def f(x):
    if x in n:
        return str(n.index(x) + 1)
    else:
        return x


with open("day1.txt") as text:
    for x in text:
        digits = [*map(f, re.findall(p, x))]
        t += int(digits[0] + digits[-1])


print(t)
