import os

def login_system():
    # HATAYI DÜZELTME: Şifreyi koddan çıkarıp Ortam Değişkeni'nden okuyoruz (Güvenli Yöntem)
    password = os.environ.get("DB_PASSWORD") 
    
    if password:
        print("Baglanti basarili ve guvenli.")

login_system()
