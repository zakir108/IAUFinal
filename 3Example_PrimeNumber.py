
#5-100 [5 is prime or not, 6 is prime or not, 7,,, 8, 9, 100 is prime or not ]

target_num = 37   # prime / N.P
d=2   # d end at 97-1| 96
flag = 0 # INITIAL FLAG VALUE = 0, will remain zero 
while d <= target_num-1:
    #print(d)   # 2,3,4,5,,,6,....34,35,36    
    if target_num%d == 0:
        flag = flag+1  # only here flag value will change, if we can divide, 97 with any of(2,3,4,..96)
        #target_num is divisible by d
    d = d+1
if flag == 0:
   print('PRIME')  
else:
   print('NON PRIME') 
