# programa que solicite para o usuário informar 3 valores e mostrar:
# o maior valor, menor valor, e o do meio

popo = []

for i in range(3):
    valor = int(input("Informe um valor: "))
    popo.append(valor)

print(popo)
popo.sort()

print("menor:", popo [0])
print("meio:", popo [1])
print("maior:", popo [2])