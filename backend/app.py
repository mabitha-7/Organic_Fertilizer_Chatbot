from flask import Flask, request, jsonify
from flask_cors import CORS
from rapidfuzz import process, fuzz

app = Flask(__name__)
CORS(app)

# Crop suggestions
soil_crops = {
    "red soil": "🌱 Red soil-க்கு தக்காளி, மிளகாய், நிலக்கடலை, கேரட் நன்றாக வளரும்.",
    "black soil": "🌾 Black soil-க்கு நெல், கரும்பு, பருத்தி நன்றாக வளரும்.",
    "sandy soil": "🌿 Sandy soil-க்கு தர்பூசணி, நிலக்கடலை, வெள்ளரி ஏற்றது.",
    "clay soil": "🌾 Clay soil-க்கு நெல் மற்றும் கோரை பயிர்கள் ஏற்றது."
}

# Fertilizer suggestions (separate flow)
fertilizer_suggestions = {
    "red soil": "🌾 Red soil-க்கு மாட்டுச் சாணம் + வெர்மி கம்போஸ்ட் சிறந்தது.",
    "black soil": "🌾 Black soil-க்கு கம்போஸ்ட் + பசளை உர பயன்படுத்தலாம்.",
    "sandy soil": "🌾 Sandy soil-க்கு அதிக கார்பன் கொண்ட இயற்கை உர நல்லது.",
    "clay soil": "🌾 Clay soil-க்கு நன்றாக கம்போஸ்ட் கலந்த உர பயன்படுத்தவும்."
}

disease_help = {
    "leaf black dots": "🍃 இலைகளில் கருப்பு புள்ளிகள் இருந்தால் வேப்பெண்ணை தெளிக்கவும்.",
    "yellow leaf": "🍂 இலை மஞ்சளாக இருந்தால் நைட்ரஜன் குறைவு இருக்கலாம்; மாட்டுச் சாணம் போடவும்."
}

greetings = ["hi", "hello", "hai", "vanakkam", "vanakam", "thanks", "thank you", "ok"]


@app.route("/")
def home():
    return "Organic Fertilizer Chatbot Backend is running ✅"


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"].lower().strip()

    # Greeting
    if any(greet in user_input for greet in greetings):
        return jsonify({
            "reply": "😊 வணக்கம்! நான் உங்கள் விவசாய உதவியாளர். எப்படி உதவலாம்?"
        })

    # 🌾 Fertilizer Recommendation Flow
    if "fertilizer" in user_input or "recommendation" in user_input:
        return jsonify({
            "reply": "🌾 எந்த மண்ணுக்கு உர பரிந்துரை வேண்டும்?\n1️⃣ Red soil\n2️⃣ Black soil\n3️⃣ Sandy soil\n4️⃣ Clay soil"
        })

    # Direct soil crop match
    for soil in soil_crops:
        if soil in user_input:
            return jsonify({"reply": soil_crops[soil]})

    # Direct fertilizer match
    for soil in fertilizer_suggestions:
        if soil in user_input:
            return jsonify({"reply": fertilizer_suggestions[soil]})

    # Disease match
    for disease in disease_help:
        if disease in user_input:
            return jsonify({"reply": disease_help[disease]})

    # 🔥 RapidFuzz fallback matching
    all_keys = list(soil_crops.keys()) + list(fertilizer_suggestions.keys()) + list(disease_help.keys())

    match = process.extractOne(
        user_input,
        all_keys,
        scorer=fuzz.partial_ratio
    )

    if match and match[1] > 60:
        key = match[0]

        if key in soil_crops:
            return jsonify({"reply": soil_crops[key]})
        elif key in fertilizer_suggestions:
            return jsonify({"reply": fertilizer_suggestions[key]})
        elif key in disease_help:
            return jsonify({"reply": disease_help[key]})

    return jsonify({
        "reply": "🤖 தயவுசெய்து மண், உர அல்லது நோய் பற்றிய கேள்வியை கேளுங்கள்."
    })


if __name__ == "__main__":
    app.run(debug=True)
