"""Kullanıcıdan değer girmesini isteyeceğiz bu değeri metre mi santimetre mi yoksa kilometre mi
gireceğini soracağız m girdiyse bunu cm ye mi yoksa km ye mi çevirmek istediğini soracağız cm istiyorsa
o değer kaç cm yapıyorsa onu ekrana yazdıracağız diğerlerini seçerse ona göre ekran çıktıları vereceğiz"""
m = "m"
cm = "cm"
km = "km"
deger = int(input("Bir değer giriniz:"))
cins = str(input("Değeri metre(m), santimetre(cm) veya kilometre(km) cinsinden mi girmek istersiniz?"))
yenicins = str(input("Dönüştürmek istediğiniz cinsi girin: "))
if cins == (m):
    if yenicins == cm:
        print(deger * 100,"santimetredir.")
    elif yenicins == km:
        print(deger * 0.001,"kilometredir.")
    else:
        print("Yanlış giriş yaptınız.")
elif cins == (cm):
    if yenicins == m:
        print(deger * 0.01, "metredir.")
    elif yenicins == km:
        print(deger * 0.001, "kilometredir.")
    else:
        print("Yanlış giriş yaptınız.")
elif cins == (km):
    if yenicins == cm:
        print(deger * 10 ** 6,"santimetredir.")
    elif yenicins == m:
        print(deger * 1000,"metredir.")
    else:
        print("Yanlış giriş yaptınız.")
else:
    print("Yanlış değer girdiniz.")
