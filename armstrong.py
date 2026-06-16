x=n=int(input("enter a number:"));
s=0;
c=0;
while(n):
    a=n%10;
    s=s+a**c;
    n=n//10;
    if(x==s):
        print("Armstrong");
    else:
        print("Not Armstrong");
