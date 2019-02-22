valor = int(input("Deseja fazer o caluculo com 2 variaveis ou 3 variaveis? :"))

if valor == 2:
    print("\nEQUAÇÃO 1\n")
    print("Quais os valores que multiplicam x e y?")
    x1 = int(input('Digite o valor que multiplica x:'))
    y1 = int(input('Digite o valor que multiplica y:'))
    resultado1 = int(input("Qual o valor do resultado da equação 1:\n"))

    soma_ou_sub1 = int(input("X e Y estão sendo somados (1) ou subtraídos (0)?:\n"))

    if soma_ou_sub1 == 1:
        print("equação1 = %s x + %s y = %s\n" % (x1, y1, resultado1))

        valor_de_multiplicação1 = int(input("Qual o valor que deseja multiplicar a equação1?:\n"))

        passo1 = valor_de_multiplicação1 * x1
        passo2 = valor_de_multiplicação1 * y1
        passo3 = valor_de_multiplicação1 * resultado1


    else:
        print("equação1 = %s x - %s y = %s\n" % (x1, y1, resultado1))

        valor_de_multiplicação1 = int(input("Qual o valor que deseja multiplicar a equação1?:\n"))

        passo1 = valor_de_multiplicação1 * x1
        passo2 = valor_de_multiplicação1 * y1
        passo3 = valor_de_multiplicação1 * resultado1

        print("EQUAÇÃO 2\n")
        print("Quais os valores que multiplicam x e y?")
        x2 = int(input('Digite o valor que multiplica x:'))
        y2 = int(input('Digite o valor que multiplica y:'))
        resultado2 = int(input("Qual o valor do resultado da equação 2:\n"))
        soma_ou_sub2 = int(input("X e Y estão sendo somados (1) ou subtraídos (0)?:\n"))

    if soma_ou_sub2 == 1:
        print("equação1 = %s x + %s y = %s\n" % (x2, y2, resultado2))

        valor_de_multiplicação2 = int(input("Qual o valor que deseja multiplicar a equação2?:\n"))

        passo4 = valor_de_multiplicação2 * x2
        passo5 = valor_de_multiplicação2 * y2
        passo6 = valor_de_multiplicação2 * resultado2


    else:
        print("equação2 = %s x - %s y = %s\n" % (x2, y2, resultado2))

        valor_de_multiplicação2 = int(input("Qual o valor que deseja multiplicar a equação2?:\n"))

        passo4 = valor_de_multiplicação2 * x2
        passo5 = valor_de_multiplicação2 * y2
        passo6 = valor_de_multiplicação2 * resultado2




elif valor == 3:
    print("Equação 1")
    x3 = int(input('Digite o valor que multiplica x:'))
    y3 = int(input('Digite o valor que multiplica y:'))
    z = int(input('Digite o valor que multiplica z:'))
    resultado3 = int(input("Qual o valor do resultado da equação 1:"))
    print("Equação 2")
    x4 = int(input('Digite o valor que multiplica x:'))
    y4 = int(input('Digite o valor que multiplica y:'))
    z1 = int(input('Digite o valor que multiplica z:'))
    resultado4 = int(input("Qual o valor do resultado da equação 2:"))

else:
    print("Numero de variaveis invalido!")
