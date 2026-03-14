text = "2026_AI_Data_Class"
# 請問 print(text[5:7]) 的輸出結果是什麼？
# (提示：索引從 0 開始，包含開頭但不包含結尾)
print(text[5:7])
# AI

skills = ["HTML", "CSS", "JS"]
skills.append("Python") # 在 skills 列表最後一個新增 Python
skills.pop(0)           # 在 skills 列表刪除第0個
# 請問現在 skills 內容是什麼？ ["CSS", "JS", "Python"]
print(skills)

for year in range(115, 121):
    if year % 2 == 0:
        print(year)
# 請問會印出哪幾個數字？ 116,118,120

user = {"name": "Uncle", "age": 43, "status": "Learning"}
# 如果要印出 "Learning"，程式碼應該怎麼寫？
# print(user[____])
print(user["status"])

a = 83
b = 13
if a > b:
    result = a
else:
    result = b
# 最終 result 的值是？這段邏輯在 Python 中還有一種簡寫，你知道嗎？
# result = a if a > b else b
# 其運作邏輯可以理解為：

# result = (a) if (a > b) else (b)

# 當條件 a > b 成立時回傳 a，否則回傳 b
# 如果要找三個數的最大值，不用 max()，你會怎麼寫？
a = 5
b = 3
c = 10
if a >= b and a >= c:
    result = a
elif b >= a and b >= c:
    result = b
else:
    result = c
# result = a if a >= b and a >= c else (b if b >= c else c)
print(result)