import random
chute = int(input('Escolha um número entre 0 e 5: '))
numRandom = random.randint(0, 5)
if chute == numRandom:
    print('Parabens, você acertou!')
else:
    print('Você errou! O número correto era {}.'.format(numRandom))
