import random
lista= []
pa = input('Primeiro aluno: ')
lista.append(pa)
sa = input('Segundo aluno: ')
lista.append(sa)
ta = input('Terceiro aluno: ')
lista.append(ta)
qa = input('Quarto aluno: ')
lista.append(qa)
random.shuffle(lista)
print(lista)
