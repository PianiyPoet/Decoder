from flask import Flask, request
from  cipher_reader import code_symbol, decode_symbol, custom_dict


def decode(phrase, dict_id):
    code_phrase = ""
    for letter in phrase:
        code_phrase += decode_symbol(dict_id, letter)
    return code_phrase


def code(phrase, dict_id):
    code_phrase = ""
    for letter in phrase:
        code_phrase += code_symbol(dict_id, letter)
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
                dict = request.form["dict"]
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
            dict = request.form["dict"]
            phrase = request.form["dec"]
            de_phrase = decode(phrase, dict)
            html = html.replace("{dhere}", f"{de_phrase}")
            return html
        else:
            return html



@app.route('/makedict', methods = ["POST","GET"])
def site_makedict():
    with open("Page_MakeDict.html", "r", encoding="utf-8") as html_stream:
        html = html_stream.read()
        if request.method == "POST":
            name = request.form["name"]
            codes = {
                "A": request.form["CODE_A"],
                "B": request.form["CODE_B"],
                "C": request.form["CODE_C"],
                "D": request.form["CODE_D"],
                "E": request.form["CODE_E"],
                "F": request.form["CODE_F"],
                "G": request.form["CODE_G"],
                "H": request.form["CODE_H"],
                "I": request.form["CODE_I"],
                "J": request.form["CODE_J"],
                "K": request.form["CODE_K"],
                "L": request.form["CODE_L"],
                "M": request.form["CODE_M"],
                "N": request.form["CODE_N"],
                "O": request.form["CODE_O"],
                "P": request.form["CODE_P"],
                "Q": request.form["CODE_Q"],
                "R": request.form["CODE_R"],
                "S": request.form["CODE_S"],
                "T": request.form["CODE_T"],
                "U": request.form["CODE_U"],
                "V": request.form["CODE_V"],
                "W": request.form["CODE_W"],
                "X": request.form["CODE_X"],
                "Y": request.form["CODE_Y"],
                "Z": request.form["CODE_Z"],

                " ": request.form["CODE_SPACE"],

                "А": request.form["CODE_CA"],
                "Б": request.form["CODE_CB"],
                "В": request.form["CODE_CV"],
                "Г": request.form["CODE_CG"],
                "Д": request.form["CODE_CD"],
                "Е": request.form["CODE_CYe"],
                "Ё": request.form["CODE_CYo"],
                "Ж": request.form["CODE_CZh"],
                "З": request.form["CODE_CZ"],
                "И": request.form["CODE_CI"],
                "Й": request.form["CODE_CJ"],
                "К": request.form["CODE_CK"],
                "Л": request.form["CODE_CL"],
                "М": request.form["CODE_CM"],
                "Н": request.form["CODE_CN"],
                "О": request.form["CODE_CO"],
                "П": request.form["CODE_CP"],
                "Р": request.form["CODE_CR"],
                "С": request.form["CODE_CS"],
                "Т": request.form["CODE_CT"],
                "У": request.form["CODE_CU"],
                "Ф": request.form["CODE_CF"],
                "Х": request.form["CODE_CKh"],
                "Ц": request.form["CODE_CTs"],
                "Ч": request.form["CODE_CCh"],
                "Ш": request.form["CODE_CSh"],
                "Щ": request.form["CODE_CSch"],
                "Ъ": request.form["CODE_CTz"],
                "Ы": request.form["CODE_CY"],
                "Ь": request.form["CODE_CMz"],
                "Э": request.form["CODE_CE"],
                "Ю": request.form["CODE_CYu"],
                "Я": request.form["CODE_CYa"],
            }
            success = custom_dict(name, codes) # 0 - все сработало правильно, 1 - ошибка
        return html
            



@app.route('/help')
def site_help():
    with open("Page_help.html", "r", encoding="utf-8") as html_stream:
        html = html_stream.read()
        return html



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')