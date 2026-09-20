def juft(sonlar):
    natija = []
    for i in sonlar:
        if i % 2 == 0:
            natija.append(i)
    return natija

sonlar = [12, 7, 5, 18, 21, 30, 44, 9]
print(juft(sonlar))       


def min_max(sonlar):
    eng_katta = eng_kichik = sonlar[0]
    for son in sonlar:
        if son > eng_katta: eng_katta = son
        if son < eng_kichik: eng_kichik = son
    print(eng_katta, eng_kichik)


sonlar = []
matn = input("Sonlarni kiriting: ")
for son in matn.split():
    sonlar.append(int(son))

min_max(sonlar)