codigos = [103,117,121,135,161,189,200,204,216]
lst = []


for codigo in codigos:
    lst.append(codigo)  if 120 <= codigo and codigo <= 200 else 0

print(f'codigos filtrados --> {lst}')