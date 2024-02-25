salario = float(input('Digite seu salário: '))
if salario > 0:
    if salario > 1250:
        aumento = salario + (salario * 0.10)
        print('Você recebeu um aumento de 10%, recebendo agora R${:.2f}'.format(aumento))
    else:
        aumento = salario + (salario * 0.15)
        print('Você recebeu um aumento de 15%, recebendo agora R${:.2f}'.format(aumento))
else:
    print('Digite um número maior que 0')
