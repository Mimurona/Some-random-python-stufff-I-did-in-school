Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print "Hello World!"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
 print "Hello World!"
 
SyntaxError: unexpected indent
print("Hello World!")
Hello World!
n=1
if(n>0):
    print("numar pozitiv")

    
numar pozitiv
2 + 2
4
(40-3*2)/4
8.5
7/3
2.3333333333333335
7/-2
-3.5
x=y=z=0
x
0
y
0

z
0
2*2.40/2
2.4
6.3/3
2.1
a=2
b=4
a+b
6
\
c=_
c
6

print("Acest program este un test variabil")
Acest program este un test variabil
'sir de caractere'
'sir de caractere'
"un alt sir de caractere"
'un alt sir de caractere'
'"Da,"a spus el.'
'"Da,"a spus el.'
"\"Da,\"a spus el."
'"Da,"a spus el.'
text = 'Acesta este un sir de caractere mai lung,\n care se intinde pe mai mai multe linii,exact ca in C.\n Observati ca spatiile de la inceputul liniei \ au importanta.'
print text
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print(text)
Acesta este un sir de caractere mai lung,
 care se intinde pe mai mai multe linii,exact ca in C.
 Observati ca spatiile de la inceputul liniei \ au importanta.
text = 'Hello' + 'World'
text
'HelloWorld'
'(' + text*3 + ')'
'(HelloWorldHelloWorldHelloWorld)'
text[6]
'o'
text[0:5]
'Hello'

================ RESTART: C:/Users/Adi/Desktop/mobile/script4.py ===============
Traceback (most recent call last):
  File "C:/Users/Adi/Desktop/mobile/script4.py", line 1, in <module>
    n=int(raw_input("Introduceti n="))
NameError: name 'raw_input' is not defined

=============== RESTART: C:/Users/Adi/Desktop/mobile/variable.py ===============
Acest program este un test pentru variabile
valoarea lui x este acum 5
x este incrementat cu 1, luand valoarea 6
x poate retine orice valoare numerica
de exemplu,x este acum 45
x inmultit cu 5 este 225

================ RESTART: C:/Users/Adi/Desktop/mobile/script4.py ===============
Traceback (most recent call last):
  File "C:/Users/Adi/Desktop/mobile/script4.py", line 1, in <module>
    n=int (raw_input("Introduceti n="))
NameError: name 'raw_input' is not defined

================ RESTART: C:/Users/Adi/Desktop/mobile/script4.py ===============
Traceback (most recent call last):
  File "C:/Users/Adi/Desktop/mobile/script4.py", line 1, in <module>
    n= raw_input("Introduceti n=")
NameError: name 'raw_input' is not defined

================ RESTART: C:/Users/Adi/Desktop/mobile/script4.py ===============
Traceback (most recent call last):
  File "C:/Users/Adi/Desktop/mobile/script4.py", line 1, in <module>
    n=int (raw_input("Introduceti n="))
NameError: name 'raw_input' is not defined

================ RESTART: C:/Users/Adi/Desktop/mobile/script5.py ===============
Traceback (most recent call last):
  File "C:/Users/Adi/Desktop/mobile/script5.py", line 1, in <module>
    x = int(raw_input("Introduceti un numar intreg: "))
NameError: name 'raw_input' is not defined

================ RESTART: C:/Users/Adi/Desktop/mobile/script5.py ===============
Traceback (most recent call last):
  File "C:/Users/Adi/Desktop/mobile/script5.py", line 1, in <module>
    x = int(raw_input("Introduceti un numar intreg: "))
NameError: name 'raw_input' is not defined

================ RESTART: C:/Users/Adi/Desktop/mobile/script5.py ===============
Traceback (most recent call last):
  File "C:/Users/Adi/Desktop/mobile/script5.py", line 1, in <module>
    x = int( raw_input("Introduceti un numar intreg: "))
NameError: name 'raw_input' is not defined

================== RESTART: C:/Users/Adi/Desktop/mobile/for.py =================
Europa 6
Asia 4
America 7

================= RESTART: C:/Users/Adi/Desktop/mobile/while.py ================
Vom afisa numerele pare pana la 20
2
4
6
8
10
12
14
16
18
20
range(10)
range(0, 10)
range (10)
range(0, 10)
range (2,10)
range(2, 10)
range (-10, -100, -30)
range(-10, -100, -30)

================= RESTART: C:/Users/Adi/Desktop/mobile/range.py ================
range (2,10)
range(2, 10)
a = ['zero','unu','doi','trei','patru','cinci']
for i in range(len(a))
SyntaxError: expected ':'
for i in range(len(a)):
    print (i, a[i])

    
0 zero
1 unu
2 doi
3 trei
4 patru
5 cinci
for n in range(2,10):
...     for x in range (2, n):
...         if n % x == 0:
...             print n, 'egal cu', x, '*', n/x
...             
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> for n in range(2,10):
...     for x in range (2, n):
...         f n % x == 0:
...             
SyntaxError: invalid syntax
>>> for n in range(2,10):
...     for x in range (2, n):
...          if n % x == 0:
...              print(n, 'egal cu', x, '*', n/x)
...              break
...             else:
...                 
SyntaxError: unindent does not match any outer indentation level
>>> for n in range(2,10):
...     for x in range (2, n):
...         if n % x == 0:
...              print(n, 'egal cu', x, '*', n/x)
...               break
...             
SyntaxError: unexpected indent
>>> for n in range(2,10):
...     for x in range (2,n):
...         if n % x == 0:
...             print(n, 'egal cu', x, '*', n/x)
...             break
...     else:
...         print(n, 'este un numar prim')
... 
...         
2 este un numar prim
3 este un numar prim
4 egal cu 2 * 2.0
5 este un numar prim
6 egal cu 2 * 3.0
7 este un numar prim
8 egal cu 2 * 4.0
9 egal cu 3 * 3.0

================= RESTART: C:/Users/Adi/Desktop/mobile/pass.py =================
