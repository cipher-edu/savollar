# Ikkita haqiqiy musbat son berilgan bo‘lsin. Ularning o‘rta arifmetik va o‘rta  geometrik qiymatlarini toping. 

x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
urta_arifmetik = (x + y) / 2
urta_arifmetik = (x * y)**0.5
print(f"O'rta arifmetik qiymat: {urta_arifmetik}")
print(f"O'rta geometrik qiymat: {urta_arifmetik}")

# x va y haqiqiy sonlar berilgan bo‘lsin. Hisoblang: min(x, y) ; 
x = float(input("x ni kiriting: "))
y = float(input("y ni kiriting: "))
minimum = min(x, y)
print("min(x, y) =", minimum)

# N natural soni berilgan boґlsin. Hisoblang : 2n!

# Foydalanuvchidan n ni olish
n = int(input("N ni kiriting: "))
factorial = 1
for i in range(1, 2*n + 1):
    factorial *= i
print(f"2n! =", factorial)

# a, b, c butun sonlar berilgan. Faqat ulardan bittasi musbatligi tekshirilsin.
a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))
c = int(input("c ni kiriting: "))
if a > 0 or b > 0 or c > 0:
    print("Faqat bitta son musbat.")
else:
    print("Barcha sonlar manfiy yoki 0.")
