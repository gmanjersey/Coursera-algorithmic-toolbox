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

