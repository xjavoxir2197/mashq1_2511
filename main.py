# 1 - misol
docs = input("Hujjat topshirildimi? (ha/yo'q): ")
interview = input("Suhbatdan o'tdingizmi? (ha/yo'q): ")
test = input("Testdan o'tdingizmi? (ha/yo'q): ")

if docs == "ha" and interview == "ha" and test == "ha":
    print("Siz ishga qabul qilindingiz!")
elif docs == "yo'q":
    print("Avvalo hujjatlaringizni topshiring.")
elif docs == "ha" and interview == "yo'q":
    print("Suhbatdan o'tmagansiz.")
elif docs == "ha" and interview == "ha" and test == "yo'q":
    print("Test natijalari yetarli emas.")
else:
    print("Jarayon davom etmoqda.")



# 2 - misol
text = input("Jumla kiriting: ")
words = text.split()
code = ""

for w in words:
    code += w[0]

print(code)


# 3 - misol
lst = [4, 7, 2, 5, 1, 10]
result = []

for i in range(len(lst)):
    result.append(lst[i] * i)

print(result)

# 4 - misol
words = ["dasturlash", "kitob", "shunday", "kompyuter", "ilm", "maktab"]

sorted_words = sorted(words, key=len, reverse=True)

print(sorted_words[0])
print(sorted_words[1])
