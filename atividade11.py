#18\. Diálogo de RPG: Crie um menu onde o jogador escolhe entre 1 (Falar), 2 (Atacar) ou 3 (Fugir). Use if/elif/else para exibir uma resposta diferente para cada escolha.
escolha = int(input("1 - Falar\\n2 - Atacar\\n3 - Fugir\\nEscolha: ")) 
if escolha == 1: print("Você escolheu falar") 
elif escolha == 2: print("Você escolheu atacar") 
elif escolha == 3: print("Você escolheu fugir") 
else: print("Opção inválida")

