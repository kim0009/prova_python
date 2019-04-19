def teorema_euclides(n):
    return ((2 ** n) - 1) * (2 ** (n - 1))

def is_primo(n):
    sqrt_n = int(n ** 1/2)
    for i in range(2, sqrt_n + 1):
        if(n % i == 0):
            return False
    return True    

def is_perfect(n, lista):
    return n in lista

t = int(input())
list_numbers_perfect = [teorema_euclides(i) for i in range(2, 10) if is_primo(i)]
i = 0
result = []

while(i < t):
    x = int(input())
    if(1 <= x <= 108):
        i += 1
        result.append(f'{x}{" eh perfeito" if is_perfect(x, list_numbers_perfect) else " não eh perfeito"}')
    else:
        print("Digite um número entre 1 e 108")

for i in result:
    print(i)