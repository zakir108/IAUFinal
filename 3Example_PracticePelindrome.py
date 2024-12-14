
s1 = 'CAc'

s2 = 'ababa'

length = len(s1)
upto = len(s1)/2 #
flag = True
pos = 0
while pos < upto-1:
    #s1[0] = s1[7]
    if s1[pos].upper() != s1[length-1 - pos  ].upper(): 
       
        flag = False
        break
    pos = pos+1

if flag == True:
    print('Pelindrome')
else:
    print('N Pelindrome')
