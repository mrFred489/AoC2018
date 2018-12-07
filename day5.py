import string as s

f = open("input5.txt")
# f = open("inputtest.txt")

old = f.read().strip()


def reduce(inp):
    for l, u in zip(s.ascii_lowercase, s.ascii_uppercase):
        inp = inp.replace(l+u, "")
        inp = inp.replace(u+l, "")
    return inp

lens = []
origin = old
for l, u in zip(s.ascii_lowercase, s.ascii_uppercase):
    old = origin.replace(l, "")
    old = old.replace(u, "")
    new = reduce(old)
    while old != new:
        old = new
        new = reduce(new)
    lens.append((len(new), l))

print(min(lens))




