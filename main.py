n = 5000
hours = n // (60 * 60)
minutes = (n - hours * 60 * 60) // 60
seconds = n - hours * 60 * 60 - minutes * 60

print(n)
print(hours)
print(minutes)
print(seconds)
print(f"{hours} : {minutes} : {seconds}")
