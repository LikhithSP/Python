x = int(input('Enter your first number>> '))
y = int(input('Enter your second number>> '))
if x > y:
    greater = x
else:
    greater = y

while True:
    if (greater % x == 0) & (greater % y == 0):
        Lcm = greater
        break
    greater += 1

print(f"LCM of {x} and {y} is {Lcm}")
