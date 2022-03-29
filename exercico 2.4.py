import random
alunos= int(input("quantos alunos"))
n1=input("primeiro aluno")
n2=input("segundo aluno")
n3=input("terceiro aluno")
n4=input("quarto aluno")
l=[n1,n2,n3,n4]
s=random.choice(l)
print("o escolhido para a pagar o quadro é {}".format(s))