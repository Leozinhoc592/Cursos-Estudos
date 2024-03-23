import random
lista = []
integrante = input('Primeiro integrante: ')
lista.append(integrante)
integrante = input('Segundo integrante: ')
lista.append(integrante)
integrante = input('Terceiro integrante: ')
lista.append(integrante)
integrante = input('Quarto integrante: ')
lista.append(integrante)
print("O escolhido foi {}".format(lista[random.randint(1,3)]))