#Receiving information from user
num = int(input("Digite um número: \n"))

# Operating with information
n = 2
count = 0

# Loop
while count < num :
    is_prime = True
    for i in range(2, n) :
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n)
        count += 1
    n += 1
