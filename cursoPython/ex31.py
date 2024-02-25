distancia = int(input('Digite a distância da viagem: '))
if 0 < distancia <= 200:
    preco = 0.50 * distancia
    print('Sua passagem custa R${:.2f}'.format(preco))
else:
    preco2 = 0.45 * distancia
    print('Sua passagem custa R${:.2f}'.format(preco2))
