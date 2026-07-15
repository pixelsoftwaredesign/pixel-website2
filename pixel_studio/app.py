from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/contact', methods=['POST'])
def handle_contact():
    data = request.json
    nom = data.get('username')
    email = data.get('useremail')
    message = data.get('usermessage')

    if not nom or not email or not message:
        return jsonify({"status": "error", "message": "Champs manquants"}), 400

    print(f"Nouveau projet reçu de {nom} ({email}) : {message[:80]}...")

    return jsonify({
        "status": "success",
        "message": "Demande enregistrée avec succès par le serveur Flask !"
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
