num = 101
while True:
    if num % 7 == 0 and num % 3 == 0:
        print(num)
        break
    num = num + 1

notas = [8.5,4.0,10.0,7.5,6.0,9.0]
soma = 0
maior = 0
for nota in notas:
    soma = soma + nota
    if nota >= 7.0:
        maior = maior + 1

med = soma / len(notas)
print(f'Média {med}')
print(f'Notas maiores que 7.0: {maior}')

lista_A = [1,2,3,4,5]
lista_B = [4,5,6,7,8]
comuns = []
for numero in lista_A:
    if numero in lista_B:
        comuns.append(numero)

print(comuns)

estoque = [
{'nome':'Teclado','preço':150.00,'quantidade':5},
{'nome':'Mouse','preço':80.00,'quantidade':12},
{'nome':'Monitor','preço':700.00,'quantidade':3},
{'nome':'Headset','preço':250.00,'quantidade':8}
]
for iten in estoque:
    if iten ['quantidade'] < 10:
        print(iten['nome'])

sku = 'PRD-004-A-v2'
sku2 = sku.replace('-', "").upper()
print(sku2)
