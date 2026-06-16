n=12546;
def count(n):
    c=0;
    while(n):
        n=n//10;
        c=c+1;
    return(c);
print(count(n));
