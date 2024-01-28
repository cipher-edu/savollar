#savol 1 Pythonda ma‘lumot turlari hamda to‘plamlari. Chiziqli dasturlar tuzish.

#savol2 A va B butun sonlar berilgan. A sonini B soniga bo`lgandagi qoldiqni toping

A = int(input('brinchi raqamni kriting'))
B = int(input('ikkinchi raqamni kriting'))

qoldiq = A % B
print(qoldiq)

#savol 3 Kiritilgan uchta sondan kattasini topuvchi dastur tuzing.

son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
son3 = int(input("Uchinchi sonni kiriting: "))

# Eng katta sonni topish
eng_katta_son = max(son1, son2, son3)

# Natijani chiqarish
print("Eng katta son:", eng_katta_son)



#savol 4.  1 dan n gacha bo‘lgan natural toq sonlarning yig`indisi topilsin.
# Foydalanuvchidan n ni olish
n = int(input("n ni kiriting: "))

# Toq sonlarni yig'indisi
yigindi = 0

for i in range(1, n+1, 2):  # 1 dan n gacha bo'lgan toq sonlar
    yigindi += i

# Natijani chiqarish
print("1 dan", n, "gacha bo'lgan toq sonlar yig'indisi:", yigindi)

#savol 5  Uch xonali son berilgan, uning birinchi raqamini oxiriga o‘tkazishdan keyingi hosil bo‘lgan son chop etilsin

# Foydalanuvchidan uch xonali sonni olish
son = int(input("Uch xonali sonni kiriting: "))

# Birinchi raqamni oxiriga o'xirish va chop etish
birinchi_raqam_oxiriga = (son % 100) * 10 + son // 100

# Natijani chiqarish
print("Birinchi raqamni oxiriga o'xirilgan son:", birinchi_raqam_oxiriga)
