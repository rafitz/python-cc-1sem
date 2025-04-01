a = int(input("A: "))
b = int(input("\nB: "))
c = int(input("\nC: "))

if a < b and a < c:
    me = a 
elif b < c:
    me = b
else: 
    me = c


if a > b and a > c:
    ma = a 
elif b > c:
    ma = b
else: 
    ma = c
print("\nMenor =", me)
print("\nMaior =", ma)