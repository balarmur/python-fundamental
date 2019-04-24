import myFunc as mf

str1 = 'apple'
lens = len(str1)
fcha = str1[0]
lcha = str1[lens-1]
bcha = str1[1:lens-1]

str2 = lcha + bcha + fcha
# print('Length of the String : ', lens)
# print('First Character      : ', fcha)
# print('Last  Character      : ', lcha)
# print('Between  Character   : ', bcha)
# print('Original String      : ', str1)
# print('Changed String       : ', str2)


str3 = 'hello'
len3 = len(str3)
str4 = str3[0::2]
#print('Changed String       : ', str4)


# list1=['one', 'two', 'three', 'four', 'five']
# for i, lst1 in enumerate(list1):
#     print("Value of i     : ", i)
#     print("Value of list1 : ", lst1)


# str4='this is a string no 04'
# lst4=list(str4)
# print("The String-4: ", str4)
# print("The List-4: ", lst4)
# lst4.pop()
# print("The List-4: ", lst4)


cs=mf.caught_speeding(51, False)
print('Ticket : ', cs)