"""
Formatação básica de strings
s -  sttring
d - int
f - float
.<numero de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
Sinal:  + ou -
ex.: 0 >-100, .1f
Conversion flags = !r !s !a
"""

variavel = 'ABC'
print(variavel)
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel:#^10}')
print(f'{1000.34573454383:+,.1f}')
print(f'{1000.34573454383:+,.1f}')

print(f' {variavel!r}')