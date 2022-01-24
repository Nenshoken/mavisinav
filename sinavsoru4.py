"""Öğrenci kayıt fonksiyonu öğrencinin adı soyadı Tcsi telefonu
maili alınacak bilgileri doğru ise öğrenci bilgileri ve kayıt tarihi
ekrana yazdırılacak TC girildiğinde 11 basamaklı olduğunu ve son basamağının
çift olduğunu kontrol edilmesi yanlış ise tekrar kullanıcıdan istenmesi Telefon numarası
ülke kodu ile girilmeli ve 12 basamaklı olması gerekir bunu kontrol edilmesi yanlış ise
tekrar girilmesi gerekmektedirMail adresinin içinde @ karakteri olup olmadığını kontrol
edilmeli yok ise tekrar girilmeli herşey
doğru ise ekrana yazdırılmalıdır ve kayıt tarihi gün ay yıl şeklinde olmalıdır"""

from datetime import datetime
def kayit():
    isim = input("Ad ve soyad: ")
    while True:

        no = input("TC numaranız: ")
        if len(str(no)) == 11 and (int(no) % 2 == 0):
            print("Tc'niz kayıt edildi.")
            break
        else:
            print("Tc yanlış girdiniz lütfen 11 haneli olmasına dikkat ediniz.")
            continue
        break
    while True:
        tel = input("Telefon numaranız: ")
        if len(str(tel)) == 12:
            print("Telefonunuz kayıt edildi.")
            break
        else:
            print("Telefon numaranızı girerken ülke kodunuz ile giriniz.")
            continue
        break
    while True:
        mail = input("Mail adresiniz: ")
        if "@" in mail:
            print("Mail adresiniz doğru.")
        else:
            print("Lütfen mail adresini yazarken '@' kullanınız")
            continue
        break
    print("İsim: {}\nTC numarası: {}\nTel No: {}\nMail: {} ".format(isim, no, tel, mail))
    suan = datetime.now()
    print(suan.day,"/", suan.month,"/", suan.year)
kayit()