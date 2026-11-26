# crie um programa que recebe números inteiros positivos um a um. valide que o número seja maior que zero.
# verifique se a sequência está semrpe crescendo, permita que o usuário pare quando quiser.
# se em algum momento o número informado for menor ou igual ao anterior, interrompa a entrada e informe que a sequência não é crescente.
# caso o usuário pare voluntariamente, informe se a sequência é crescente ou não. exiba a soma e a quantidade de números informados.
# obs: len = quantidade


print("digite 0 para encerrar o programa.")
while True:
    numeros = []

    while True:
        valor = int(input("informe um número: "))
        if valor == 0:
            print(f"end.\nsequência: {numeros}.\nsoma: {sum(numeros)}.\nquantidade: {len(numeros)} ")
        elif valor < 0:
            print("o número deve ser maior que zero.")
        
        elif len(numeros) > 0 and valor <= numeros[-1]:  # [] colchetes busca posição, () chama função
            print("a sequência não é crescente.")
            break
        numeros.append(valor)

    if input("iniciar novamente? (y/n): ") != "y": #  se for diferente de 'y' não reinicia, encerra
            break   