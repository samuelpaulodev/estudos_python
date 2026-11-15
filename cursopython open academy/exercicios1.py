#exercio do notbook lm, criar as variaveis
nome_produto = "Monitor Gamer 27"
quantidade = 2
preco_unitario = 1250.90
em_estoque = True
#calcular os valor total

valor_total = quantidade * preco_unitario

#agora vamos exibir na tela
print("=== RESUMO DA VENDA ===")
print(f"Produto: { nome_produto}")
# o print(F) serve pra inserir alguma variavel dentro da string printada
print(f"Quantitade: {quantidade}")
print(f"Preço unitario: {preco_unitario}")
print(f"Valor Total: {valor_total}")
print(f"Disponivel em Estoque: {em_estoque}")