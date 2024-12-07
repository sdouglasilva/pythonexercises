# Faça um Programa que leia 5 números digitados pelo usuário
#  e coloque-os em uma lista. Imprima a lista no console. Não crie 5 variáveis.
lista = []
for i in range(5):
    numero = int(input('Digite um número para adicionar na lista'))
    lista.append(numero)

print(lista)