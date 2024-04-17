user = "Andrey" #Это будет логин
name = "d1" #Это название словаря (введено пользователем)
fulname = f"{user}_{name}"
#Ниже словарь, загруженный пользователем
text_file = """a ☯
b ☸
c ☮
d ☦
e ✙
f ☤
g ◄
h ⇐
i ➟
j ↘
k ↺
l ⇉
m ✔
n ☑
o ♻
p ▰
q ▓
r ☠
s ┴
t ✯
u ❆
v ☀
w ♙
x ✾
y ☂
z ☭
  §"""
with open(f"{fulname}.txt", mode="w", encoding="utf-8") as t_file: #Сохранение в тхт (не уверен, что оно нужно)
  t_file.write(text_file)

fil = open(f"{fulname}.txt", "r", encoding="utf-8") #Выгрузка из тхт, если пользователь загрузил файл в таком формате
text_file = fil.read()
fil.close()
dict = {}
text_file = text_file.split("\n") #Превращение строки в словарь
for sym in text_file:
  dict[sym[0]] = sym[2:]
print(dict)