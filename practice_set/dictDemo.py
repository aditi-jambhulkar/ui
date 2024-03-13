sample_dict = {"name": "Kelly","age": 25,"salary": 8000,"city": "New york"}
keys = ["name", "salary"]

newDic = {}
for key in sample_dict:
    if key not in keys:
        newDic[key] = sample_dict[key]
print(newDic)