fh = open("test.txt", "w")
fh.write("first line\nsecond line\nthird line")
fh.close()

fh = open("test.txt", "r")
lines = [el.strip() for el in fh.readlines()]
print(lines)

fh.close()
