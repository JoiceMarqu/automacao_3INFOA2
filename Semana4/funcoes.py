'''
As funções permite modularizar o código,dividir ele em partes
menores que podem ser reaproveitadas.Isso simplifica a 
codificação.

Estrutura função em python

def nome_funcao(entrada1,entrada2,entradaN);
     //algum codigo que a função faz 
     return saída_da_funcao
'''
#cria uma função que calucula a área do triângulo
def calculaTriânguloArea(base,altura):
        (base * altura) / 2
        return area

#cria uma função que calucula a área do triângulo
def calculateSquareArea(lado):
        area = lado * lado
        return area

'''
#Exemplo 1:chamar a função
area1 = calculateTriânguloArea(100,10)
print("A área do Triângulo 1 é: ",area1)

#Exemplo 2:Chmar a função novamente
base =float(input('Digite a base:'))
altura =float(input('Digite a altura'))
area2 = caclculaTriânguloArea(base,altura)
print("A área do triângulo 2 é:",area2)
'''