"""Mevcudu bilinmeyen bir sınıf için 1 sınav notu için sınıf ortalaması hesaplanacak
Öğrencinin adı soyadı ayrı istenilecek daha sonra o öğrencinin sınav notu
istenilecek daha sonra isim soyisim ve öğrencinin notu ekrana yazdırılacak.
Öğrenci not girme işleminden sonra sınıf ortalaması ekrana yazdırılacak"""

toplam = 0
digerOgrenciNotlari = [58,75,90,34,27]
ad = input("Adınız: ")
soyad = input("Soyadınız: ")
notu = int(input("Sınav notunuz: "))
print("{} {} isimli {} notlu öğrenci.".format(ad, soyad, notu))
digerOgrenciNotlari.append(notu)
toplam = sum(digerOgrenciNotlari)
adet = len(digerOgrenciNotlari)
print("Sınıf ortalaması; ",toplam / adet)
#notları istediğimiz gibi arttırabiliriz.