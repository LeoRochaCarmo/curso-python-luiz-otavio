#%%

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)

#%%
print(f'{numero_3:.2f}') # retornar uma string
print(type(f'{numero_3:.2f}')) 
print(round(numero_3, 2)) # retornar um float
print(type(round(numero_3, 2)))

#%%
# usando o módulo decimal
import decimal
numero_1 = decimal.Decimal(0.1)
numero_2 = decimal.Decimal(0.7)
numero_3 = numero_1 + numero_2
print(numero_3)
# %%
