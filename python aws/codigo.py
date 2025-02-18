print("This numbers are prime:")
primos = []
for x in range(2,250):
    eh_primo = True
    for i in range(2,x):
        if x % i == 0:
            eh_primo = False
            break
    if eh_primo:
        print(x)
        primos.append(x)

with open("results.txt", "w") as file:
    for primo in primos:
        file.write(str(primo) + '\n')
print("Arquivo de teste foi criado")

