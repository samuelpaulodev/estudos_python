#adcionar dados usando o input e converter pra int e float
nome_loja = input("DIgite o nome da sua loja:")
#o input adciona um dado pra dentro e o que ta entre aspas é o placeholder
vendas_dia = int(input("Quantas vendas foram realizadas hoje?"))
#colocar o int() e o Input() dentro do int transforma o dado que entra em inteiro
ticket_medio = float(input("Qual o valor médio de cada venda(RS)? "))
#mesma coisa com o float()

#calcular o faturamento
faturamento = vendas_dia *ticket_medio

#printando

print("\n--- RELATÓRIO DIÁRIO ---")
#\n serve pra quebra de linha
print(f"Loja: {nome_loja}")
print(f"Total de vendas: {vendas_dia}")
print(F"Faturamento estimado: R$ {faturamento:.2f}")
"""O trecho :.2f dentro da f-string é um formatador de números decimais (float). Ele serve para controlar exatamente como um número deve ser exibido na tela.

Dividindo por partes, cada caractere tem uma função específica:

    : (dois-pontos): Separa o nome da variável das regras de formatação.

    .2: Significa que você quer exatamente 2 casas decimais após o ponto.

    f: Significa fixed-point (ponto fixo), que é o formato padrão para números decimais (floats)."""