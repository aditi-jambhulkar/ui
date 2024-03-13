# lst=[]
# how_many_element=int(input("enter how many element="))
#
# for i in range(0, how_many_element):
#
#         lst.append(int(input("enter the element=")))
#
#         print(i, end=' ')

#
# which_element_remove=int(input('enter the element to remove='))
# lst.remove(which_element_remove)
# for i in lst:
#      print(i, end=',')


#reverse order
# list=[3,6,2,7,8,1,9]
# print(list[: : -1])

#add two list index wise
# list1 = ["M", "na","i","ke"]
# list2 = ["y","me","s","lly"]
# res = list1[0] + list2[0],  list1[1] + list2[1],list1[2] + list2[2], list1[3] + list2[3]
# print(res)

# list1 = ["M", "na","i","ke"]
# list2 = ["y","me","s","lly"]

# for x,y in zip(list1,list2):
#     print(x+y)





#program in to turn square
# numbers =[1,2,3,4,5,6,7]
# for i in numbers:
#     print(i*i, end=',')

#concatination
# list1 =["hello" , "take"]
# list2 =["dear" , "sir"]
# for x in list1:
#     for y in list2:
#         print(x +" "+y)

#zip funtion and reversing
# list1 =[10,20,30,40]
# list2 =[100,200,300,400]
# for x,y in zip(list1,list2[: : -1]):
#     print(x,y)

#replace and value
# list1 =[5, 10,15, 20,25, 50,20]
# ind =list1.index(20)
# list1[ind] = 200
# print(list1)

#remove all occurrence of itam 20
# list1 =[5, 20, 15, 20, 25, 50,20]
# while 20 in list1:
#     list1.remove(20)
#     print(list1)

# for i in list1:
#     if i == 20:
#         list1.remove(20)
# print(list1)


# list1 = ["mike", "", "emma", 'kelly',"", 'brad']
# res = list(filter(None, list1))
# print(res)

# lst=[]
# how_many_element=int(input("enter how many element="))
#
# for i in range(0, how_many_element):
#
#          lst.append(int(input("enter the element =")))
# oreder = input('enter the order as a and b =')
# if oreder == ('a'):
#     lst.sort(reverse=True)
#     for i in lst:
#         print(i, end=' ')
# elif oreder == ('b'):
#     lst.sort(reverse=False)
#     for i in lst:
#         print(i, end=' ')
# else:
#     print(None)