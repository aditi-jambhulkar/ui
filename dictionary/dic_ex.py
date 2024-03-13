#Python is Good Programing Language

# dic = {"upper":0,"lower":0}
# dic1 = input('enter the string name =')
# upper_count = 0
# lower_count = 0
# for char in dic1:
#     if char.isupper():
#          dic["upper"] += 1
#
#
#     elif char.lower():

#         dic["lower"] +=1
#     else:
#         pass
#         print("the number of uppercase char is =",dic["upper"])
#         print('the number of lowercase char is =',dic["lower"])



# dic = {"alpha":0,"number":0}
# dic1 = input('enter the string name =')
# alpha_char = 0
# num_count = 0
# for char in dic1:
#     if char.isalpha():
#         dic['alpha'] += 1
#     elif char.isnumeric():
#         dic['number'] += 1
# else:
#     print("the number of alpha char is =", dic['alpha'])
#     print('the number of number char is =', dic['number'])

dic = {"alpha":0,"number":0}
dic1 = input('enter the string name =')
alpha_char = 0
num_count = 0
for char in dic1:
    if char.isalnum():
        dic["alpha"] += 1
    elif char.isnumeric():
        dic['num'] += 1
    else:
        print(dic["alpha"])
        print(dic["num"])