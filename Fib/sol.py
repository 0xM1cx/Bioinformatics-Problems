def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)

with open('./rosalind_fibo.txt') as f:
    n = int(f.readline().strip())
        

    print(fib(n))