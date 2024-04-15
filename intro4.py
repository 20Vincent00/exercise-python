cours = input("Entrez le nom du cours svp:")
nom = input("Entrez votre nom svp:")
prog = input("Entrez le # du programme svp:")
print(len(cours))
for char in cours:
    print(char)
complete = "%s, %s, %s" %(cours, nom, prog)
print(complete)
fmt = (cours, nom, prog)
complete = "%s, %s, %s" %fmt
print(complete)

complete = "{one}, {two}, {three}" .format(one=cours, two=nom, three=prog)
print(complete)