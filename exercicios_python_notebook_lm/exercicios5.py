#analise de credito usando and or
idade = int(input(" Informe sua idade. "))
renda = float(input(" Informe a sua renda. "))
nome_limpo = input("com 'sim' ou 'nao', informe se seu nome é limpo ")
limpo = nome_limpo == 'sim' and nome_limpo != 'nao'

if idade>=21 and renda>=3000.0 and limpo == True:
    print("Aprovado")
else:
    print("Negado")


