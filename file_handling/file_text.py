# q 1 Write a program that writes 10 random numbers to a file 'numbers.txt'.
# Each random number should be in the range of 1 through 100.
# import random
#
# file_path = 'D:\pythonfilehandling\python1.txt'
# fp =open(file_path,'w')
# for i in range(10):
#     number=random.randint(1,100)
#     fp.write(str(number)+'\n')
# fp.close()


# Write a function in python to count the number of lines from a text file "story.txt"
# which is not starting with an alphabet "T".Example: If the file "story.txt" contains the following lines:
# A boy is playing there.There is a playground.An airplane is in the sky.The sky is pink.
# Alphabets and numbers are allowed in the password.
# The function should display the output as 3

# count = 0
# with open("D:\pythonfilehandling\story.txt",'r')as fp:
#     for i in fp:
#         if i[0] not in 'T':
#             count = count + 1
# print("count",count)

# count=0
# with open("D:\pythonfilehandling\story.txt",'r')as fp:
#     for i in fp:
#         if i[0] in "T":
#             count = count +1
# print(count)

# count =0
# with open('D:\pythonfilehandling\story.txt','r')as fp:
#     for i in fp:
#         if i.startswith("A"):
#          count = count +1
# print(count)


# Write a function in Python to read lines from a text file "notes.txt". Your function should find and display
# the occurrence of the word "the".For example: If the content of the file is:
# "India is the fastest-growing economy. India is looking for more investments around the globe.
# The whole world is looking at India as a great market.
# Most of the Indians can foresee the heights that India is capable of reaching."

# The output should be 5
# count = 0
# with open(r"D:\pythonfilehandling\notes.txt",'r')as fp:
#     content = fp.read()
#     word = content.split()
#     for i in word:
#         if i == 'the' or i == 'The':
#             count = count +1
# print(count)
