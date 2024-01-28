# savol 2. A va B butun sonlar berilgan. A sonini B soniga bo`lgandagi butun qismni toping.

A = int(input("A ni kiriting: "))
B = int(input("B ni kiriting: "))
butun_qism = A // B
print("A ni B ga bo'lgandagi butun qism:", butun_qism)

#savol 3. Kiritilgan uchta sondan kichigini topuvchi dastur tuzing.
son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
son3 = int(input("Uchinchi sonni kiriting: "))
kichik_son = min(son1, son2, son3)
print("Uchta sonning eng kichigi:", kichik_son)

#1 dan n gacha bo`lgan natural ichidan 5ga karrali sonlarning yig`indisi topilsin.

n = int(input("n ni kiriting: "))
yigindi = 0
for i in range(1, n+1, 5): 
    yigindi += i
print("1 dan", n, "gacha bo'lgan 5ga karrali sonlar yig'indisi:", yigindi)

#Uch xonali son berilgan. Uning o‘nlik va birlik xonalaridagi raqamlarini almashtirish natijasida hosil bo’lgan son chop etilsin.
uch_xonali_son = int(input("Uch xonali sonni kiriting: "))
o = uch_xonali_son // 10
b = uch_xonali_son % 10

almashtirilgan_son = b * 10 + o
print("Almashtirilgan son:", almashtirilgan_son)
