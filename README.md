# Documentação do Repositório

1. Este código reúne diferentes mini-programas em Python para praticar conceitos como **laços**, **listas**, **dicionários**, **condições** e **manipulação de strings**.

---

## Objetivo

* Compreender o uso de loops (`while`, `for`)
* Calcular média e contagem em listas
* Identificar elementos comuns entre listas
* Filtrar itens em dicionários
* Manipular strings com `.replace()` e `.upper()`

---

## Passos realizados

### **1 – Encontrar o primeiro número divisível por 3 e 7**

1. Inicia em 101 e procura o primeiro número múltiplo de 3 e 7.

   ```python
   num = 101
   while True:
       if num % 7 == 0 and num % 3 == 0:
           print(num)
           break
       num = num + 1
   ```

**Aprendizado:** Uso de `while`, operadores matemáticos e condição múltipla.

---

### **2 – Média e quantidade de notas maiores ou iguais a 7**

1. Soma todas as notas e calcula a média.
2. Conta quantas notas são ≥ 7.0.

   ```python
   notas = [8.5,4.0,10.0,7.5,6.0,9.0]
   soma = 0
   maior = 0
   for nota in notas:
       soma = soma + nota
       if nota >= 7.0:
           maior = maior + 1

   med = soma / len(notas)
   print(med)
   print(maior)
   ```

**Aprendizado:** Iteração por listas, contagem e média.

---

### **3 – Encontrar elementos em comum entre duas listas**

1. Compara os itens das listas A e B.
2. Adiciona os elementos iguais à nova lista.

   ```python
   lista_A = [1,2,3,4,5]
   lista_B = [4,5,6,7,8]
   comuns = []
   for itenA in lista_A:
       if itenA in lista_B:
           comuns.append(itenA)

   print(comuns)
   ```

**Aprendizado:** Uso do operador `in` e construção dinâmica de listas.

---

### **4 – Exibir produtos com estoque baixo**

1. Verifica produtos com quantidade menor que 10 e exibe o nome.

   ```python
   estoque = [
   {'nome':'Teclado','preço':150.00,'quantidade':5},
   {'nome':'Mouse','preço':80.00,'quantidade':12},
   {'nome':'Monitor','preço':700.00,'quantidade':3},
   {'nome':'Headset','preço':250.00,'quantidade':8}
   ]
   for iten in estoque:
       if iten['quantidade'] < 10:
           print(iten['nome'])
   ```

**Aprendizado:** Iteração em listas de dicionários.

---

### **5 – Formatação de código SKU**

1. Remove os hífens e converte para maiúsculo.

   ```python
   sku = 'PRD-004-A-v2'
   sku2 = sku.replace('-', "").upper()
   print(sku2)
   ```

**Aprendizado:** Manipulação de strings com métodos nativos.

---
