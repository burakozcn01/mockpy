#!/usr/bin/env python
"""
MockPy Hızlı Başlangıç Örneği

Bu basit script, python-mockpy kütüphanesinin temel kullanımını gösterir.
En sık kullanılan veri üretim fonksiyonlarını içerir.
"""

from mockpy import MockPy
import json

# MockPy örneği oluştur (Türkçe veriler için)
mock = MockPy(locale="tr_TR")
print("MockPy Hızlı Başlangıç - Gerçekçi Test Verileri\n")

# 1. Kişi bilgileri
person = mock.person.person()
print("✅ KİŞİ BİLGİLERİ:")
print(f"   Ad Soyad: {person.full_name}")
print(f"   E-posta: {person.email}")
print(f"   Telefon: {person.phone}")
print(f"   Doğum: {person.birth_date} ({person.age} yaş)")

# 2. Adres bilgileri
address = mock.address.address()
print("\n✅ ADRES BİLGİLERİ:")
print(f"   Sokak: {address.street}")
print(f"   Şehir: {address.city}")
print(f"   Ülke: {address.country}")
print(f"   Posta Kodu: {address.postal_code}")

# 3. Şirket bilgileri
company = mock.company.company()
print("\n✅ ŞİRKET BİLGİLERİ:")
print(f"   Şirket Adı: {company.name}")
print(f"   Web Sitesi: {company.website}")
print(f"   Sektör: {company.industry}")
print(f"   Kuruluş Yılı: {company.founded}")

# 4. Finansal bilgiler
cc = mock.finance.credit_card()
print("\n✅ FİNANSAL BİLGİLER:")
print(f"   Kart: {cc.formatted_number}")
print(f"   Tür: {cc.type}")
print(f"   Son Kullanma: {cc.expiration}")
print(f"   IBAN: {mock.finance.iban()}")

# 5. İnternet bilgileri
print("\n✅ İNTERNET BİLGİLERİ:")
print(f"   Kullanıcı Adı: {mock.internet.user_name()}")
print(f"   Şifre: {mock.internet.password()}")
print(f"   URL: {mock.internet.url()}")
print(f"   IP: {mock.internet.ip_v4()}")

# 6. Şema tabanlı veri üretimi
print("\n✅ ŞEMA TABANLI VERİ ÜRETİMİ:")
schema = {
    "id": {"type": "integer", "min": 1000, "max": 9999},
    "name": {"type": "lorem", "words": 3},
    "price": {"type": "float", "min": 10.0, "max": 500.0, "precision": 2},
    "category": {"type": "choice", "choices": ["Elektronik", "Giyim", "Kitap", "Oyuncak", "Spor"]},
    "in_stock": {"type": "choice", "choices": [True, False]},
    "rating": {"type": "float", "min": 1.0, "max": 5.0, "precision": 1}
}

# 2 ürün üret ve to_dict() ile JSON'a dönüştür
products = mock.generate_dataset(schema, count=2)
products_dict = [p if isinstance(p, dict) else p.to_dict() for p in products]
print(json.dumps(products_dict, indent=2, ensure_ascii=False))

# 7. İngilizce veri örneği (farklı locale)
en_mock = MockPy(locale="en_US")
en_person = en_mock.person.person()

print("\n✅ ENGLISH DATA EXAMPLE:")
print(f"   Name: {en_person.full_name}")
print(f"   Email: {en_person.email}")
print(f"   Address: {en_mock.address.street_address()}, {en_mock.address.city()}")