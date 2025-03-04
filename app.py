from flask import Flask, render_template, request
import logging

app = Flask(__name__)

# Hata kaydını etkinleştir
logging.basicConfig(level=logging.DEBUG)

# Karbon ayak izi hesaplama fonksiyonu
def calculate_carbon_footprint(transport, electricity, diet):
    score = 0
    
    # Ulaşım
    if transport == "walking":
        score += 0
    elif transport == "bike":
        score += 1
    elif transport == "bus":
        score += 3
    elif transport == "car":
        score += 6
    
    # Elektrik kullanımı
    if electricity == "low":
        score += 2
    elif electricity == "medium":
        score += 4
    elif electricity == "high":
        score += 6
    
    # Beslenme alışkanlıkları
    if diet == "vegetarian":
        score += 2
    elif diet == "balanced":
        score += 4
    elif diet == "meat":
        score += 6
    
    return score

@app.route("/", methods=["GET", "POST"])
def index():
    try:
        if request.method == "POST":
            transport = request.form.get("transport", "").strip()
            electricity = request.form.get("electricity", "").strip()
            diet = request.form.get("diet", "").strip()

            # Eksik veri olup olmadığını kontrol et
            if not transport or not electricity or not diet:
                app.logger.error("Eksik veri girdisi!")
                return "HATA: Eksik bilgi girdiniz, lütfen tüm alanları doldurun!", 400

            app.logger.info(f"Form verisi: transport={transport}, electricity={electricity}, diet={diet}")
            
            score = calculate_carbon_footprint(transport, electricity, diet)
            
            if score <= 6:
                result = "Harika! Çevreci bir kahramansın! 🌿"
            elif score <= 12:
                result = "Fena değil ama daha dikkatli olmalısın! ⚠️"
            else:
                result = "Çevre için daha dikkatli olmalısın! 🚨"
            
            return render_template("result.html", score=score, result=result)

        return render_template("index.html")

    except Exception as e:
        app.logger.error(f"Beklenmedik hata: {str(e)}")
        return "Sunucuda bir hata oluştu. Lütfen tekrar deneyin.", 500

if __name__ == "__main__":
    app.run(debug=True)
