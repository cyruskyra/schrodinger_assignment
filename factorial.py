def fact(no):
    n = no
    ans = no
    while n > 1:
        n -= 1
        print n
        ans = ans*n
    
    return ans
