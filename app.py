from flask import Flask, render_template
app = Flask(__name__)

menu = [
    {"name": "Маргарита", "ingredients": "Томати, моцарела, базилік", "price": 120},
    {"name": "Пепероні", "ingredients": "Пепероні, томатний соус, сир", "price": 150},
    {"name": "Чотири сири", "ingredients": "Моцарела, горгонзола, пармезан, чеддер", "price": 180},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu_page():
    return render_template('menu.html', menu=menu)

if __name__ == '__main__':
    app.run(port=1234, debug=True)