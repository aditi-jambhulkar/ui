#
# import os
#
# file_path = "D:\pythonfilehandling\python4.txt"
# if os.path.exists(file_path):
#     print('file is present')
# else:
#     try:
#         with open(file_path,'w') as fp:
#             fp.write('file creat successfuly.')
#     except FileNotFoundError as err:
#         print(err)

# ------------------------------------------------------------------------------------------------

# import os
#
# file_path = input('enter the location file =')
# final_path = file_path + '.txt'
# if os.path.exists(final_path):
#     print("file already exists")
# else:
#     try:
#         with open(final_path,'w') as fp:
#             fp.write('file create sucessfully.')
#     except FileNotFoundError as err:
#         print(err)

# -------------------------------------------------------------------------------
# import random
# #
# num= random.randint(1,999)
# file_path = input('enter the location ...=')
# file_path = file_path + '.txt'
# if os.path.exists(file_path):
#     print('file is exit')
# else:
#     try:
#         with open(file_path, 'a') as fp:
#             fp.write('file creat successfully.')
#     except FileNotFoundError as err:
#         print('file not found', err)