import string

a= 'A'
b= 'B'
c= 1.1

formato1 = 'a={} b={} c={:.2f}'.format(a,b,c)

formato2 = 'a={0} b={1} c={2:.2f}'.format(a,b,c) #indice

string= 'a={nome1} b={nome2} c={nome3:.2f}'
formato3 = string.format(
    nome1= a
    ,nome2= b
    ,nome3= c
)
print(formato1)
print(formato3)
print(formato3)

nome = "Luiz"
idade = 23
formato = '{n} tem {i} anos'
print(formato.format(n=nome, i=idade))