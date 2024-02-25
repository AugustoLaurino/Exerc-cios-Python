import random
nome1 = str(input('Digite o primeiro nome: '))
nome2 = str(input('Digite o segundo nome: '))
nome3 = str(input('Digite o terceiro nome: '))
nome4 = str(input('Digite o quarto nome: '))
nomes = [nome1, nome2, nome3, nome4]
sortear = random.choice(nomes)
print('O aluno escolhido foi {}'.format(sortear))