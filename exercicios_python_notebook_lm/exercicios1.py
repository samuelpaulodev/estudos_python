#pedir ao usuario para digitar seu nome, idade e altura
#converter idade para int e altura pra float
#printar tudo na tela e mostrar o tipo de altura

nome = input("Digite seu nome")
idade = int(input("Digite sua idade"))
altura = float(input("Digite sua altura"))
tipo_altura = type(altura)

print(f"Seu nome é: {nome}, sua idade é: {idade} e sua altura é: {altura}")
print(f"Além disso, sua altura é um dado do tipo {tipo_altura}")