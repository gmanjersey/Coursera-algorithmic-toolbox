#msg = "Hello World."
#print(msg)
#msg.lower()

#print(8/5)   # = 1.6
#print (17%3) #modulus = 2
#print(17//3) #floor division discard the fractional part = 5
#print(17/3)  # = 5.666666666666667
#print(5**2) #5 squared
import sys

my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
print(my_dict)
print(type(my_dict))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.get('Dave'))


def firstUniqueueChar(s):
    hashMap=dict()
    index = 0
    for c in s:
     print(c)
     if(not(hashMap.get(c) )):
        hashMap[c] = index
     else:
        hashMap[c] = -1

    min = sys.maxsize
   
    for c1 in hashMap:
      if(hashMap[c] > -1 and hashMap[c] < min) :
          min = hashMap[c]

    return -1 if min == sys.maxsize else min




    # print(hashMap.get(c))


print("Fist Uniqueue Character Index is :" + str(firstUniqueueChar("Leetcode")))

     