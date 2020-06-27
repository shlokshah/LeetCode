def palindrome(x):
    xs=x
    xr=0
    if x<0:
        return False
    else:
        while xs>0:
            xr=xr*10+(xs%10)
            xs=xs//10
        return xr==x


