def juft(sonlar):
    natija = []
    for i in sonlar:
        if i % 2 == 0:
            natija.append(i)
    return natija

sonlar = [12, 7, 5, 18, 21, 30, 44, 9]
print(juft(sonlar))       
