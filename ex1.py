f = [0, 1]
def fib(n: int) -> int:
    if(n > (len(f) - 1)):
        for i in range(len(f), n + 1):
            f.append(f[i - 1] + f[i - 2])
    return f[n]

t = int(input())
i = 0
result = []
while(i < t):
    n = int(input())
    if(0 <= n <= 60):
        i += 1
        result.append(f'Fib({n}) = {fib(n)}')
    else:
        print("Digite um número entre 0 e 60")


for i in result:
    print(i)

