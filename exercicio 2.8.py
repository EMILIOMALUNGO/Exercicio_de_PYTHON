
nome=str(input("digita uma frase")).lower().strip()

print("veja quantas vezes aperece a letra (A):{}".format(nome.count("a")))
print("que posição ela se encontra a primera vez: {}".format(nome.find("a")))
print("que posição ela se encontrava pela   a ultima vez:{}".format(nome.rfind("a")))