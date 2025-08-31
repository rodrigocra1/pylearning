x = 1
while x > 0:
    x = int(input("Digite x: "))
    if x == 0:
        print("Digitaste zero.")
        break
    print(x)
else:
    print("Digitaste negativo")

print("Fim")