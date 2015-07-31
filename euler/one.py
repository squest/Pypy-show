import time

def sol1 (lim) :
    res = 0
    for i in xrange (1,lim) :
        if 0 == i % 3 or 0 == i % 5:
            res += i
    return res

def sol2 (lim) :
    res,a,b,tmp = 0,1,0,0
    while True :
        if a > lim :
            return res
        tmp = a
        a += b
        b = tmp
        if 0 == a % 2:
            res += a
    return res

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def odd_prime (n):
    for i in xrange (3,isqrt (n) + 1,2):
        if 0 == n % i:
            return False
    return True

def sol3 (target) :
    n,i, cur = target , 3, target
    while True :
        if odd_prime (i) :
            while 0 == n % i :
                n /= i
            if n == 1 :
                return cur
            else :
                cur = n
        i += 2

def sol3b (target):
    n,i = target,3
    while not (odd_prime (n)):
        while (not (odd_prime (i))) and (0 != n % i):
            i += 2
        while 0 == n % i :
            n /= i
        i += 2
    return n

def numcol(n):
    tar, res = n, []
    while tar >= 10 :
        res.append(tar % 10)
        tar /= 10
    res.append(tar)
    res.reverse()
    return res

def is_palin(n):
    tmp = numcol(n)
    tmp1 = list.reverse(tmp)
    return tmp1 == tmp

def sol4 (lim) :
    maxi = 0
    for i in xrange(800,lim-1):
        for j in xrange(i+1,lim):
            tmp = i*j
            if is_palin(tmp):
                maxi = max(maxi,tmp)
    return maxi



def timex (st,f,x):
    print(st)
    start_time = time.time()
    tmp = f(x)
    print (tmp)
    print("--- %s seconds ---" % (time.time() - start_time))

timex ("No 1 ", sol1, 1000)
timex ("No 2 ", sol2, 4000000)
timex ("No 3 : ", sol3, 600851475143)
timex ("No 3b : ", sol3b, 600851475143)
timex ("No 4 : ", sol4, 999)
