from flask import Flask, render_template

app = Flask(__name__)

# Главная страница с нашим тренажером
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Запускаем локальный сервер на порту 5000
    app.write = print
    print("🚀 Сервер запущен! Откройте в браузере: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)