def my_sum(*a, b = 'hello') : #packing
    s = 0
    for i in a:
        s+=i
    return s

print( my_sum(1,2,3,4) ) #unpacking
print( 1,2,3,4, sep="-",end="끝" ) #default parameters === sep=' ', end: '\n'
