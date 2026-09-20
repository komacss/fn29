# def juft(sonlar):
#     natija = []
#     for i in sonlar:
#         if i % 2 == 0:
#             natija.append(i)
#     return natija

# sonlar = [12, 7, 5, 18, 21, 30, 44, 9]
# print(juft(sonlar))       


# def min_max(sonlar):
#     eng_katta = eng_kichik = sonlar[0]
#     for son in sonlar:
#         if son > eng_katta: eng_katta = son
#         if son < eng_kichik: eng_kichik = son
#     print(eng_katta, eng_kichik)


# sonlar = []
# matn = input("Sonlarni kiriting: ")
# for son in matn.split():
#     sonlar.append(int(son))

# min_max(sonlar)


# def qimmat_mahsulotlar(a):
#     for nomi, narx in a.items():
#         if narx > 15000:
#             print(nomi, "-", narx)
# mahsulotlar = {
#     "non": 4000,
#     "sut": 10000,
#     "shakar": 14000,
#     "yog'": 18000,
#     "guruch": 16000
# }

# qimmat_mahsulotlar(mahsulotlar)


# def natijalar(baholar):
#     for ism in baholar:
#         bahosi = baholar[ism]
#         if bahosi >= 60:
#             print(ism, "-", bahosi, "-", "O'tdi")
#         else:
#             print(ism, "-", bahosi, "-", "Yiqildi")

# baholar = {
#     "Ali": 78,
#     "Vali": 45,
#     "Hasan": 91,
#     "Husan": 56,
#     "Sardor": 67
# }

# natijalar(baholar)


# def takrorlanmas_sonlar(sonlar):
#     yangi_list = []
#     for son in sonlar:
#         if son not in yangi_list:
#             yangi_list.append(son)
#     return yangi_list


# sonlar = [2, 5, 2, 8, 5, 9, 2, 8, 10, 5]
# print(takrorlanmas_sonlar(sonlar))


# def kontakt_qidir(kontaktlar, ism):
#     if ism in kontaktlar:
#         print(kontaktlar[ism])
#     else:
#         print("Bunday kontakt topilmadi")


# kontaktlar = {
#     "Ali": "901234567",
#     "Vali": "911112233"
# }

# ism = input("Ism kiriting: ")
# kontakt_qidir(kontaktlar, ism)

# def son_topish(sirli_son):
#     while True:
#         son = int(input("Son kiriting: "))
#         if son > sirli_son:
#             print("Kichikroq son kiriting")
#         elif son < sirli_son:
#             print("Kattaroq son kiriting")
#         else:
#             print("Tabriklayman!")
#             break


# sirli_son = 37
# son_topish(sirli_son)

# def savat_hisobla(mahsulotlar):
#     jami = 0
#     while True:
#         nomi = input("Mahsulot kiriting: ")
#         if nomi == "stop":
#             break
#         if nomi in mahsulotlar:
#             jami = jami + mahsulotlar[nomi]
#     print("Umumiy narx:", jami)


# mahsulotlar = {
#     "non": 4000,
#     "sut": 10000,
#     "shakar": 14000,
#     "guruch": 16000,
#     "yog'": 18000
# }

# savat_hisobla(mahsulotlar)

# def statistika(oquvchilar):
#     otganlar = 0
#     yiqilganlar = 0
#     eng_yuqori = eng_past = None
#     jami = 0
#     soni = 0

#     for ism in oquvchilar:
#         bali = oquvchilar[ism]
#         soni = soni + 1
#         jami = jami + bali

#         if bali >= 60:
#             otganlar = otganlar + 1
#         else:
#             yiqilganlar = yiqilganlar + 1

#         if eng_yuqori is None or bali > eng_yuqori:
#             eng_yuqori = bali
#         if eng_past is None or bali < eng_past:
#             eng_past = bali

#     ortacha = jami / soni

#     print("O'tganlar:", otganlar)
#     print("Yiqilganlar:", yiqilganlar)
#     print("Eng yuqori ball:", eng_yuqori)
#     print("Eng past ball:", eng_past)
#     print("O'rtacha ball:", ortacha)


# oquvchilar = {
#     "Ali": 85,
#     "Vali": 45,
#     "Hasan": 72,
#     "Husan": 58,
#     "Sardor": 91,
#     "Jasur": 63
# }

# statistika(oquvchilar)


def mahsulotlarni_korsatish(mahsulotlar):
    for nomi in mahsulotlar:
        print(nomi, "-", mahsulotlar[nomi])


def savatga_qoshish(mahsulotlar, savat):
    nomi = input("Mahsulot nomini kiriting: ")
    if nomi in mahsulotlar:
        savat.append(nomi)
        print("Qo'shildi!")
    else:
        print("Bunday mahsulot yo'q")
    return savat


def savatni_korsatish(savat):
    for nomi in savat:
        print(nomi)


def umumiy_narx(mahsulotlar, savat):
    jami = 0
    for nomi in savat:
        jami += mahsulotlar[nomi]
    return jami


mahsulotlar = {
    "olma": 12000,
    "banan": 18000,
    "apelsin": 15000,
    "uzum": 20000,
    "anor": 25000
}

savat = []

while True:
    print("1. Mahsulotlarni ko'rish")
    print("2. Savatga mahsulot qo'shish")
    print("3. Savatni ko'rish")
    print("4. Umumiy narxni ko'rish")
    print("5. Dasturdan chiqish")

    tanlov = input("Tanlovni kiriting: ")

    if tanlov == "1":
        mahsulotlarni_korsatish(mahsulotlar)
    elif tanlov == "2":
        savat = savatga_qoshish(mahsulotlar, savat)
    elif tanlov == "3":
        savatni_korsatish(savat)
    elif tanlov == "4":
        print("Umumiy narx:", umumiy_narx(mahsulotlar, savat))
    elif tanlov == "5":
        break
    else:
        print("Noto'g'ri tanlov")