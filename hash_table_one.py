# Criando uma hash table (dicionário)
hash_table = {}

# Adicionando chave-valor na hash table
hash_table['nome'] = 'Maria'
hash_table['idade'] = 25
hash_table['cidade'] = 'Rio de Janeiro'

# Acessando um valor usando a chave
print("Nome:", hash_table['nome'])  # Output: Maria

# Verificando se uma chave existe
if 'idade' in hash_table:
    print("Idade:", hash_table['idade'])  # Output: 25

# Atualizando um valor
hash_table['idade'] = 26

# Excluindo um par chave-valor
del hash_table['cidade']

# Iterando sobre as chaves e valores
for chave, valor in hash_table.items():
    print(f'{chave}: {valor}')

# Exemplo de uma hash table com números
hash_table_numeros = {1: 'um', 2: 'dois', 3: 'três'}
print(hash_table_numeros[2])  # Output: dois
