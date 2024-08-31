print("Enter a Even Number:")
a=int(input())
if a==2:
    print("2 cannot be given :(")
elif a%2 ==1:
    print(a,"is not an Even Number :(")
elif a==0:
    print("Null Number has been Entered")
while a>2 and a%2==0:
     print("Enter a Number Until Even Number to be Displayed")
     b=int(input())
     for c in range(a,b+1):
         if c%2 ==0:
             print(a)
             a+=2

