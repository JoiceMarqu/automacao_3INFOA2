'''
Exercício 3 - Semana 3
Crie um programa que lê do teclado
sucessivos números de matricula (int).
O programa deve parar de ler os números 
quando a matricula 0 for digitada.
Ao final deve apresentar os números de 
matriculas separados em 3 grupos.
'''
grupo 1 []
grupo 2 []
grupo 3 []
 
 while true:
      matricula = int(input("Digite o número da matricula (digite 0 para parar): "))
      if matricula == 0:
         break
      
      if matricula % 3 == 0:
         grupo1.append(matricula)

      elif matricula % 3 == 1:
         grupo2.append(matricula)

      else
         grupo3.append(matricula)

print("Grupo 1: " grupo1)
print("Grupo 2: " grupo2)
print("Grupo 3: " grupo3)