# solicitar 2 numeros ao usuario e fazer operações com ele
numero_1 = int(input("Digite aqui o primeiro numero "))
numero_2 = int(input("Digite aqui o segundo numero numero "))

soma = numero_1 + numero_2
divisao_inteira = numero_1 // numero_2
resto = numero_1 % numero_2
exponenciacao = numero_1 ** numero_2

print(f"A soma de {numero_1} com {numero_2} é: {soma}. \n A divisão inteira é: {divisao_inteira}. \n O resto é: {resto}. \n e por fim o a exponenciação é: {exponenciacao}.")