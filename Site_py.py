from flask import Flask, request


c_dict = {
"a":"☯",
"b":"☸",
"c":"☮",
"d":"☦",
"e":"✙",
"f":"☤",
"g":"◄",
"h":"⇐",
"i":"➟",
"j":"↘",
"k":"↺",
"l":"⇉",
"m":"✔",
"n":"☑",
"o":"♻",
"p":"▰",
"q":"▓",
"r":"☠",
"s":"┴",
"t":"✯",
"u":"❆",
"v":"☀",
"w":"♙",
"x":"✾",
"y":"☂",
"z":"☭",
" ":"§"
}

de_dict = {}
for sym in c_dict:
    de_dict[c_dict[sym]] = sym


def code(phrase, c_dict):
    code_phrase = ""
    for letter in phrase:
        if letter in c_dict:
            code_phrase += c_dict[letter]
        else:
            code_phrase += letter
    return code_phrase



def decode(phrase, dec_dict):
    code_phrase = ""
    for letter in phrase:
        if letter in dec_dict:
            code_phrase += dec_dict[letter]
        else:
            code_phrase += letter
    return code_phrase

app = Flask(__name__)


@app.route('/')
def site_home():
    with open("Page_home.html", "r", encoding="utf-8") as html_stream:
        html = html_stream.read()
        return html


@app.route('/code', methods = ["POST", "GET"])
def site_code():
    with open("Page_code.html", "r", encoding="utf-8") as html_stream:
        html = html_stream.read()
        if request.method == "POST":
                dict = c_dict
                phrase = request.form["nm"]
                c_phrase = code(phrase, dict)
                html = html.replace("{chere}", f"{c_phrase}")
                return html
        else:
            return html



@app.route('/decode', methods = ["POST","GET"])
def site_decode():
    with open("Page_decode.html", "r", encoding="utf-8") as html_stream:
        html = html_stream.read()
        if request.method == "POST":
            dict = de_dict
            phrase = request.form["dec"]
            de_phrase = decode(phrase, dict)
            html = html.replace("{dhere}", f"{de_phrase}")
            return html
        else:
            return html



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')