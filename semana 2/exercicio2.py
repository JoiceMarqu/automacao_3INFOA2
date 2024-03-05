'''
Exercício 2:
Crie um programa que lê do teclado a nota
e a quantidade de faltas de um aluno. O
programa deve imprimir reprovado, se:
A nota for menor que 6 ou se as presencas
forem menor do que 75 e aprovado 
caso contrário.
'''
Nota  = int (input("Digite a nota do aluno: "))
Faltas = int (input("Digite a quantidade de faltas do aluno: "))

if Nota > 6 :
    print(Nota," Aluno Aprovado")
else:
    print(Nota,"Aluno Reprovado")

if Faltas > 75 :
    print(Faltas,"Aluno Reprovado")
else:
    print(Faltas,"Aluno Aprovado")