from flask import Flask, jsonify, render_template
from flask_talisman import Talisman

app = Flask(__name__)
talisman = Talisman(app, content_security_policy=None, force_https=True)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')  # Render index.html template

@app.route('/horaire')
def horaire():
    return render_template('horaire.html')  # Render horaire.html template

@app.route('/menu')
def menu():
    return render_template('menu.html')  # Render menu.html template
    
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong"})  # Return JSON response {"message": "pong"}

if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=5001, debug=True)
