#%%
# Secrets para gerar números aleatórios

import secrets

# seleciona um número abaixo de 100
print(secrets.randbelow(100))

# seleciona um item dentro da lista
print(secrets.choice([10, 11, 12]))

# gera uma sequência de bytes aleatórios
secrets.token_bytes(10)

# cria uma senha em hexadecimal (sem pontuação)
print(secrets.token_hex(10))

#%%
# Transformando o módulo random com números aleátorios seguros
random = secrets.SystemRandom()

r_range = random.randrange(10, 100, 2)
print(r_range)

#%%
# Criando senha forte com 12 caracteres
import string as s
from secrets import SystemRandom as sr

random = sr()

letters = s.ascii_letters + s.digits + s.punctuation
random_password = ''.join(random.choices(letters, k=12))
print(random_password)






