
while True:
    try:
        vize1 = int(input("İlk vize Sonucunuzu Giriniz : "))

        break
    except:
        print("Girdiğiniz Değer Geçersizdir")

        continue
while vize1 > 100 or vize1 < 0:
        print("Lütfen Geçerli bir değer giriniz")
        vize1 = int(input("İlk vize Sonucunuzu Giriniz : "))
while True:
    try:
        vize2 = int(input("İkinci vize Sonucunuzu Giriniz : "))

        break
    except:
        print("Girdiğiniz Değer Geçersizdir")

        continue
while vize2 > 100 or vize2 < 0:
        print("Lütfen Geçerli bir değer giriniz")
        vize2 = int(input("İkinci vize Sonucunuzu Giriniz : "))
while True:
    try:
        final = int(input("Final Sonucunuzu Giriniz : "))

        break
    except:
        print("Girdiğiniz Değer Geçersizdir")
        continue
while final > 100 or final < 0:
        print("Lütfen Geçerli bir değer giriniz")
        final = (input("İlk vize Sonucunuzu Giriniz : "))
sonuc = int(float(vize1)*(3/10)) + (float(vize2)*(3/10)) + (float(final)*(4/10))
if sonuc >= 90:
    print("Ortalama Notunuuz :", sonuc, "ve Harf Notunuz AA dır")
elif sonuc >= 85:
    print("Ortalama Notunuuz :", sonuc, "ve Harf Notunuz BA dır")
elif sonuc >= 80:
    print("Ortalama Notunuuz :", sonuc, "ve Harf Notunuz BB dır")
elif sonuc >= 75:
    print("Ortalama Notunuuz :", sonuc, "ve Harf Notunuz CB dır")
elif sonuc >= 70:
    print("Ortalama Notunuuz :", sonuc, "ve Harf Notunuz CC dır")
elif sonuc >= 65:
    print("Ortalama Notunuuz :", sonuc, "ve Harf Notunuz DC dır")
elif sonuc >= 60:
    print("Ortalama Notunuuz :", sonuc, "ve Harf Notunuz DD dır")
elif sonuc >= 55:
    print("Ortalama Notunuuz :", sonuc, "ve Harf Notunuz FD dır")
elif sonuc >= 50:
    print("Ortalama Notunuuz :", sonuc, "ve Harf Notunuz FF dır")
else:
    print("Sen bu dersi alttan al geçmiş olsun :(((")
