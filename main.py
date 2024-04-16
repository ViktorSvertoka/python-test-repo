def convert_camel_to_snake(name):
    res = ""
    for char in name:
        if char.isupper():
            res += "_" + char.lower()
        else:
            res += char
    return res


s = "geeksForGeeks"

snaked_s = convert_camel_to_snake(s)

print(snaked_s)
