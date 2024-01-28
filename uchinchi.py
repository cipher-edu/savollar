# x va y haqiqiy sonlar berilgan bo‘lsin. Hisoblang: 
 # x va y haqiqiy sonlarni olish
x = float(input("x ni kiriting: "))
y = float(input("y ni kiriting: "))
natija = x**2 + y**2
print("x^2 + y^2 =", natija)

# Kiritilgan uchta sondan kattasini topuvchi dastur tuzing.
# Uchta sonni foydalanuvchidan olish
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
son3 = float(input("Uchinchi sonni kiriting: "))
katta_son = max(son1, son2, son3)
print("Uchta sonlarning eng kattasi:", katta_son)


# A va B butun sonlar berilgan. A dan B gacha bo`lgan natural toq sonlarning yig`indisi topilsin.
A = int(input("A ni kiriting: "))
B = int(input("B ni kiriting: "))
yigindi = 0

for i in range(A, B+1):
    if i % 2 == 1: 
        yigindi += i
print(f"{A} dan {B} gacha bo'lgan toq sonlar yig'indisi:", yigindi)

# Sutkaning n-sekundi bo‘lsa, sutka boshidan buyon necha minut o‘tganligi aniqlansin.
n = int(input("Sekundlarni kiriting: "))
minutlar = n // 60
print(f"{n} sekund {minutlar} minutga teng keladi.")
