# for文の使い方 (簡易)

users_info = [["Bob", 79], ["Tom", 59], ["Ken", 61]]

for user in users_info:
    name = user[0]
    age = user[1]

print(f"Name:{name}, Age:{age}")

# ken 61 しか出てこない
