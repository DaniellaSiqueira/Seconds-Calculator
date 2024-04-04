dia = int(input('digite a quantidade de dias: '))
hora = int(input('digite a quantidade de horas: '))
minutos = int(input('digite a quantidade de minutos: '))
segundos = int(input('digite a quantidade de segundos: '))
dia = dia * 86400
hora = hora * 3600
minutos = minutos * 60
tempo = dia + hora + minutos + segundos
print (f'o tempo em segundos é de: {tempo}')

