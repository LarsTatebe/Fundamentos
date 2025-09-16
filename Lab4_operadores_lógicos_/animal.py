a = input("Primeira palavra: ")
b = input("Segunda palavra: ")
c = input("Terceira palavra: ")

if a == "invertebrado":
    if b == "inseto":
        resultado = "pulga" if c == "hematofago" else "lagarta"
    elif b == "anelideo":
        resultado = "sanguessuga" if c == "hematofago" else "minhoca"
    else:
        resultado = "animal desconhecido"
elif a == "vertebrado":
    if b == "mamifero":
        resultado = "homem" if c == "onivoro" else "vaca"
    elif b == "ave":
        resultado = "aguia" if c == "carnivoro" else "pomba"
    else:
        resultado = "animal desconhecido"
else:
    resultado = "animal desconhecido"

print(resultado)