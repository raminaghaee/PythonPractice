'''
*
**
***
****
*****
'''
for i in range(1,6):
    print(i*"*")
##===============================================
'''
1
22
333
4444
55555
'''

for i in range(1,6):
    print(i* str(i))
##===============================================

'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''
rows = 5
for i in range(rows ,0 ,-1):
    num = i
    for j in range(1,i+1):
        print(j, end=" \t")
    print("\r")
#================================================
'''
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
'''

rows = 5
for i in range(rows ,0 ,-1):
    num = i
    for j in range(i,0,-1):
        print(j, end=" \t")
    print("\r")
