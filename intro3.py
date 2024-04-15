calcul = str(2) + ' + ' + str(2) + ' = quatre'
print(calcul)

calcul = "%d + %d = %s" %(5, 5, "dix")
print(calcul)

fmt = (5, 5, "dix")
calcul = "%d + %d = %s" %fmt
print(calcul)

calcul = "{chiffre} + {chiffre} = {mot}" .format(chiffre=5, mot="dix")
print(calcul)