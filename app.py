from flask import Flask, render_template, request

app = Flask(__name__)

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
    if request.method == "POST":
        transport = request.form.get("transport")
        electricity = request.form.get("electricity")
        diet = request.form.get("diet")
        
        score = calculate_carbon_footprint(transport, electricity, diet)
        
        if score <= 6:
            result = "Harika! Çevreci bir kahramansın! 🌿"
        elif score <= 12:
            result = "Fena değil ama daha dikkatli olmalısın! ⚠️"
        else:
            result = "Çevre için daha dikkatli olmalısın! 🚨"
        
        re
