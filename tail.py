def tailrec(n,num):
    if n > num:
        return
    
    print(n)
    
    tailrec(n+1,num)
     
n = int(input("Enter number to print 1 to number: "))
tailrec(1,n)