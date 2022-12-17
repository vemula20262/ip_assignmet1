n = int(input("enter the value of n: "))
k = 1
def pattern (n,k):
    while k <= n:
        print("*" * k + " " * 2 * (n - k) + "*" * k)
        k += 1

pattern(n,k)



