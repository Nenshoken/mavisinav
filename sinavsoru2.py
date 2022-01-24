"""Kullanıcıya 4 çeşit yiyecek ve 4 çeşit içecek listelenecek kullanıcı
bu 4 yiyecek ve 4 içecekten sipariş verecek siparişi bittikten sonra sipariş
verdiği ürünler ekrana yazdırılacak ve o ürünlerin ücretleri toplamı ekrana yazıdırılacak."""

hesap = 0
menu = []
yiyecek = ["doner", "kebap", "kofte", "makarna"]
icecek = ["su", "ayran", "kola", "gazoz"]
donerdeger = 10
kebapdeger = 20
koftedeger = 15
makarnadeger = 5
sudeger = 2
ayrandeger = 3
koladeger = 6
gazozdeger = 4

print(yiyecek)
print(icecek)
print("Siparişi tamamlamak için 0 tuşuna basınız.")
while True:
    siparis = input("İstediğiniz yiyecek ve içeceği seçiniz: ")
    menu.append(siparis)
    if siparis == "0":
        break
    else:
        print("Siparişiniz alındı.")
for x in menu:
    if (x == 'gazoz'):
        hesap = hesap + gazozdeger
    elif(x == 'kebap'):
        hesap = hesap + kebapdeger
    elif(x == 'kofte'):
        hesap = hesap + koftedeger
    elif(x == 'makarna'):
        hesap = hesap + makarnadeger
    elif(x == 'su'):
        hesap = hesap + sudeger
    elif(x == 'ayran'):
        hesap = hesap + ayrandeger
    elif(x == 'kola'):
        hesap = hesap + koladeger
    elif(x == 'doner'):
        hesap = hesap + donerdeger
    else:
        print("Menüde öyle bir yiyecek yada içecek yer almamakta.")

print("Yedikleriniz: ",menu)
print("Hesabınız: ",hesap,"Tl")
