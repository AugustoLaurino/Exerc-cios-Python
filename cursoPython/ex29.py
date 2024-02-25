v = int(input('Digite a velocidade do carro: '))
if v > 80:
    print('MULTADO !Você excedeu o limite permitido que é de 80km/h.')
    multa = (v-80) * 7
    print('Você recebeu uma multa de R${}'.format(multa))
print('Tenha um Bom Dia, dirija com cuidado!')
