PH = float(input("Digite um valor do PH: "))
if PH < 6.0:
    r = "Ácida"
elif PH < 7.0:
    r = "Levemente ácida"
elif PH == 7.0:
    r = "Neutra"
elif PH < 8.0:
    r = "Levemente alcalina"
else:
    r = "Alcalina"

print(f"Com pH = {PH} a solução é {r}")