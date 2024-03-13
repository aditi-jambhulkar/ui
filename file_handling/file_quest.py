 # q 2 Write a program that reads and display all of the numbers stored in the file numbers.
# txt (created in question 1) and calculates their total.

import  random
total = 0
with open('D:\pythonfilehandling\python1.txt','r')as fp:
        for i in fp:
            print(i)

            total = total + int(i)
print("total",total)

# ------------------------------------------------------------------------------------------------------------

#  q 3 Write a function, digit_count() in Python that counts and displays the number of digits in the
# text file named 'sample.txt'. For example, if the content of 'sample.txt' is as follows :
 # The team achieved a milestone in 2023. They completed a multi-million-dollar project ahead of schedule.
 # Stakeholders were impressed with a 98% success rate.
# The function return output as 6.

# count = 0
# with open('D:\pythonfilehandling\sampl.txt','r') as fp:
#     content = fp.read()
#     for i in content:
#         if i.isdigit():
#           count = count + 1
#     print(count)

# --------------------------------------------------------------------------------------------------------------


 # 4 Write a function lines_count() that reads lines from a text file named 'zen.txt' and displays
 # the lines that begin with any vowel. Assume the file contains the following text and already exists
 # on the computer's disk:
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# The lines_count() function should display the output as:
# Explicit is better than implicit.

# list =['a', 'e', 'i', 'o','u']
# with open('D:\pythonfilehandling\zen.txt','r') as fp:zsxdcfghyjuikolp;[']+++/

#     for i in fp:
#         if i[0].lower() in list:
#             print(i)

# ----------------------------------------------------------------------------------------------------------------

# q 5 Assume that the file 'notes.txt' containing some text and exists on the computer’s disk.
 # Write a program that display only those words from 'notes.txt' file whose length is more than seven.
 # Keep in mind that any punctuation marks at the beginning or end of a word should also be considered as part
 # of the word's length.


# with open('D:\pythonfilehandling\zen.txt','r')as fp:
#     content = fp.read()
# words = content.split()
# print('word with length more than seven =')
# for word in words:
#     if len(word)> 7:
#         print(word)

# --------------------------------------------------------------------------------------------------------------

# 6. Write a function last_digit_words() in Python to count the words ending with a digit in a text file
#  "notes.txt". For example, if the file content is as follows :

# The Computer6 hums softly as I sit with a Book3 in hand, diving into a world of imagination.
#  Outside, my friends gather at House9 and I quickly grab my Pen2 to jot down the address.

# The expected output should be:Number of words ending with a digit are 4

# with open('D:\pythonfilehandling\\note.txt','r')as fp:
#     content = fp.read()
#     word = content.split()
#     count = 0
#     for i in word:
#         if i[-1].isdigit():
#             print(i)
#             count = count+1
# print(count)

#----------------------------------------------------------------------------------------------------------

# 7. Assume that a file 'names.txt' containing a series of names (as strings) exists on the computer’s disk.
 # Write a function, first_five() that displays only the first five lines of the file’s contents.
 # If the file contains less than five lines,
 # it should display the file’s entire contents.

# with open("D:\\pythonfilehandling\\note.txt",'r')as fp:
#      content = fp.readlines()
#      for i in content[0:5]:
#          print(i)

# -------------------------------------------------------------------------------------------
# q = 8 Write a Python program that reads a text file and prints its contents in reverse order
 # (from the last line to the first line)

# with open("D:\pythonfilehandling\content.txt",'r')as fp:
#     result = fp.read()
#     print(result[::-1])


# Q 9 = Assume that a file named 'feedback.txt' contains student feedback in the following format:
# Positive: Saksham improved grades, more confident now.
# Negative: Arav needs better time management for coursework.
# Negative: Samar should work on communication in group activities.
# Negative: Soham could benefit from asking more questions in class.
# Positive: Sakshi excels academically, a great team player.
# Write a Python function named feedback_analysis() to calculate and display the following information:
# Total feedbacks stored in the file.
# Count of positive feedbacks.
# Count of negative feedbacks

# totalcount= 0
# positivefeedback = 0
# negativefeedback = 0
# with open(r"D:\pythonfilehandling\feedback.txt",'r') as fp:
#     for i in fp:
#        totalcount = totalcount + 1
#        if i.startswith('Positive'):
#            positivefeedback = positivefeedback +1
#        elif i.startswith('Negative'):
#            negativefeedback = negativefeedback +1
# print(totalcount)
# print(positivefeedback)
# print(negativefeedback)



