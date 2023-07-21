#Este projeto visa criar um sistema de compra e pagamento de supermercado usando programação procedural
#Nome: Matheus
#Data: 20/07/2023

# Importando módulos
import csv
from mercado_menu import mercado_opcoes

# Introdução
print("=====BEM-VINDO AO SUPERMERCADO JCAVI=====\n")

nome = input("Qual o seu nome? ").capitalize()

print("\nOlá, %s! Estes são os itens disponíveis em nossa loja:\n" % (nome))

# Menu de itens
for chave, produto in mercado_opcoes.items():
    print(f"{chave} - {produto[0]} = R${produto[1]}")

# Seleção de itens
carrinho = []

def carrinho_compras():
    while True:
        escolha = int(input("Digite o número do produto que deseja adicionar ao carrinho ou '0' para finalizar a compra: "))

        if escolha == 0:
            break

        if escolha in mercado_opcoes:
            print("Essas foram suas escolhas\n")

            carrinho.append(escolha)

            print(carrinho)
            print(f"Item '{escolha}' adicionado ao carrinho.")
        else:
            print("Item não encontrado. Por favor, escolha outro.")


carrinho_compras()

print("Suas opções foram enviadas ao carrinho")

for escolha in carrinho:
    print(f"- {escolha} {mercado_opcoes[escolha][0]}")

valor_total = sum([mercado_opcoes[escolha][1] for escolha in carrinho])

# Pagamento
print(f"Certo. Agora escolha a forma de pagamento.\n1 - Dinheiro > 5% de desconto!\n2 - Débito > 5% de desconto!\n3 - Crédito > Sem desconto! :(")
pagamento = input("Como deseja pagar sua compra? ")
def pagar(valor_total):
    desconto = 1-0.05
    if pagamento == 1 or pagamento == 2:
        return valor_total * desconto
    elif pagamento == 3:
        return valor_total
    else:
        return ("Opção Indisponível. Digite Apenas uma das Opções Acima!")
    
print("Pagamento realizado. Obrigado e volte sempre, %s!"% (nome))

# Exportar opções para arquivo CSV
with open("carrinho.csv", "w", newline="") as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    for item in carrinho:
        writer.writerow([item])
