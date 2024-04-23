import sqlite3


def code_symbol(id, symbol):
    db = sqlite3.connect("ciphers.sqlite")
    cur = db.cursor()
    try:
        table = cur.execute(f"""SELECT dict FROM main AS m
                            WHERE m.id = {id}""").fetchall()[0][0]
        coded_symb = cur.execute(f"""SELECT code FROM {table} AS t
                                 WHERE t.symbol = '{symbol.upper()}'""").fetchall()[0][0]
    except Exception:
        coded_symb = "-"
    db.close()
    return coded_symb


def decode_symbol(id, symbol):
    db = sqlite3.connect("ciphers.sqlite")
    cur = db.cursor()
    try:
        table = cur.execute(f"""SELECT dict FROM main AS m
                            WHERE m.id = {id}""").fetchall()[0][0]
        decoded_symb = cur.execute(f"""SELECT symbol FROM {table} AS t
                                   WHERE t.code = '{symbol}'""").fetchall()[0][0]
    except Exception:
        decoded_symb = "-"
    db.close()
    return decoded_symb


def custom_dict(name, symbols):
    db = sqlite3.connect("ciphers.sqlite")
    cur = db.cursor()
    tables = cur.execute(f"""SELECT dict FROM main""").fetchall()
    if name == "" or (name,) in tables:
        return 1
    cur.execute(f"""CREATE TABLE {name} (
                    symbol STRING PRIMARY KEY
                                  UNIQUE
                                  NOT NULL,
                    code STRING  NOT NULL
                                 UNIQUE
                );""").fetchall()
    for symb, code in symbols.items():
        cur.execute(f"""INSERT INTO {name}(symbol,code) VALUES('{symb}','{code}') """).fetchall()
    ids = cur.execute(f"""SELECT id FROM main""").fetchall()
    new_id = ids[-1][0] + 1
    print(new_id)
    cur.execute(f"""INSERT INTO main(id,dict) VALUES('{new_id}','{name}') """).fetchall()
    db.commit()
    db.close()
    return 0


if __name__ == "__main__":
    custom_dict("test", {"A": "t", "B": "y"})