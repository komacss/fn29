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


def takrorlanmas_sonlar(sonlar):
    yangi_list = []
    for son in sonlar:
        if son not in yangi_list:
            yangi_list.append(son)
    return yangi_list


sonlar = [2, 5, 2, 8, 5, 9, 2, 8, 10, 5]
print(takrorlanmas_sonlar(sonlar))