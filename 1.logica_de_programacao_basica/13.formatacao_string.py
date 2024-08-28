#FORMATAÇÃO DE STRING COM .FORMAT ()

a = 'A'
b = 'B'
c = 1.1

string = 'a={nome1} b={nome2} c={nome3:.2f} d={nome3}'
formato = string.format(
    nome1=a, 
    nome2=b, 
    nome3=c
    )

print(formato)