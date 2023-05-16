"""
list = ['Bikash','Sangam','Puru','Nabin']
for x in range(len(list)):
    print(list[x]);
"""
#To print prime number 
indx1 = int(input('Enter the inital number: '))
indx2 = int(input('Enter the last number: '))

for num in range (indx1,indx2+1):
    if(indx1>1):
        isDivisible = False;
        for index in range(2,num):
            if num%index == 0:
                isDivisible = True;
        if not isDivisible:
            print(num);
                
