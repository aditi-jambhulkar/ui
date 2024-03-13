# t1 = (1, 2, 3, 4,5)
# t2 = ('java ', 'python')
#
# print(t1 + t2)
# print(t1 *3)
# print(t1[3])
# print(t1 [: -1: 2])
# print(1 in t1)
# print(t1 is t2)
# print("adress of t1 is =",id(t1))


# tup = (1,2,3,4,5,6,6,7,8,9)
# length = len(tup)
# count = tup.count(6)
# print(length)
# print(count)
# tup1 = (1,2,3)
# tup2 = (4,5,6)
# result = tup1+tup2
# print(result)


# tup = (10,30,40,20,50)
# exists = 30 in tup
# print(exists)

# tup = (1,2,3)
# str = str(tup)
# print(str)

# index = tup.index(2)
# print(index)

# tup = (1,2,3,4,5)
# for element in tup:
    # print(element)
# max = max(tup)
# print(max)

# tuple = ('h','e','l','l','o')
#
# str = ','.join(tuple)
# print(str)


# Solution:
def tuple_to_single_string(tup):
    return ''.join(tup)

tup = ('H', 'e', 'l', 'l', 'o')
result = tuple_to_single_string(tup)
print(result)  # Output: "Hello"