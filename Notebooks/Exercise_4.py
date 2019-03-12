#!/home/user/miniconda3/bin/python

## Question_1 Creating a while loop that starts with x = 0 and increments x until x is equal to 5. Each iteration should print to the console

x = 0
while x <= 5:
    print(x+1)
    x = x+1
    print("Ready for boarding")
    
    
## Question_2:loop above skips printing x = 5 to the console but will print values of x from 6 to 10

for x in range(10):
    if x==4:
        print("",x)
        continue
    print("Ready for boarding",x)
    
    
## Question_3:Creating a for loop that prints values from 4 to 10 to the console

for x in range(10):
    if x<3:
        print("",x)
        continue
    print("Ready for boarding",x)