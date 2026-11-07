#10\. Par ou Ímpar: Peça um número ao usuário. Use o operador % e uma estrutura if/else para dizer se o número é par ou ímpar.
#* Se for 7 ou mais: "Aprovado".
#* Se for entre 5 e 6.9: "Recuperação".
#* Se for menor que 5: "Reprovado".
#que receba a nota de um aluno:
numero = int(input("Digite um número: ")) 
if numero % 2 == 0: print("Número par") 
else: print("Número ímpar")

