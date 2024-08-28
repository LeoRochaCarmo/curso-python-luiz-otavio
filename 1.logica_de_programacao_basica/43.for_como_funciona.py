"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

text = iter('Leo') #iterável
iterador = iter(text) #iterator

while True: 
    try:
        print(next(iterador))
    except StopIteration:
        break