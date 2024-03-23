import math
angulo = float(input('Qual o angulo?'))
cosseno = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('No angulo de {:.2f}° temos seno={:.2f},coseno={:.2f} e tangente={:.2f}'.format(angulo,seno,cosseno,tangente))