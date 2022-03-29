nome=str(input("nome de uma cidade")).strip()


print("O nome da tua cidade começa com bauru?:{}".format(nome[:5].upper() == "BAURU"))