
piramidStart = 1
piramidend = 5

starCount=1 #1,3,5,7
spaceCount = piramidend-1

while piramidStart <=piramidend: #1,2,3,4,5
    
    space= spaceCount          
    while space>=1:
        print('-',end='')
        space=space-1    
    
    starBegin = 1
    while starBegin<=starCount:  #  1,2,3,4,5 | 1,3,5,7,9    
        print("*", end='')
        starBegin=starBegin+1
    print()
    
    
    
    piramidStart = piramidStart+1
    starCount = starCount+2
    spaceCount = spaceCount-1