import os
space=10
for row in range(10,0,-1):
    space=space+1
    print(' '*space,end='')
    
    for col in range(0,row):
        
        print("*",end='')
    print(end='\n')
