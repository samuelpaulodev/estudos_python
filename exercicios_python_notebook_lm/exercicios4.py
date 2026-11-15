#calcular o imc usando if elif else
peso = float(input("Digite o seu peso. "))
altura = float(input("Digite sua altura. "))
imc = peso / (altura ** 2)
print(f" seu IMC é {imc:.2f}. ")

if imc<18.5:
    print("Abaixo do peso")
elif imc <=25.0:
    print("Peso Normal")
elif imc <=30.0:
    print("Sobrepeso")
else:
    print("Obesidade")