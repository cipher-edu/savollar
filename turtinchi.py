# Kubning qirrasi  ma’lum bo‘lsa,  uning yon sirti va hajmi topilsin. 
qirra = float(input("Kubning qirrasini kiriting: "))
yon_sirti = 6 * qirra**2
hajmi = qirra**3
print(f"Kubning yon sirti: {yon_sirti}")
print(f"Kubning hajmi: {hajmi}")

# x va y haqiqiy sonlar berilgan bo‘lsin. Hisoblang: a)  max(x, y);  
x = float(input("x ni kiriting: "))
y = float(input("y ni kiriting: "))
maksimum = max(x, y)
print("max(x, y) =", maksimum)

# N natural soni berilgan boґlsin. Hisoblang :  1+2+3+…+n
n = int(input("N ni kiriting: "))
yigindi = sum(range(1, n+1))
print(f"1+2+3+...+{n} =", yigindi)

# a, b, c butun sonlar berilgan. Ularning hech bo‘lmaganda bittasi musbat ekanligi tekshirilsin
a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))
c = int(input("c ni kiriting: "))
if a > 0 or b > 0 or c > 0:
    print("Hech bo'lmaganda bitta son musbat.")
else:
    print("Hech bo'lmaganda bitta son musbat emas.")
