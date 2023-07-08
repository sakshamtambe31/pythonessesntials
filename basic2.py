Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
id(x)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    id(x)
NameError: name 'x' is not defined
x
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    x
NameError: name 'x' is not defined
x=10
y=10
id(x)
2194414961168
id(y)
2194414961168
print(keyword.kwlist)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(keyword.kwlist)
NameError: name 'keyword' is not defined
import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
X=[2,5.4,(6+9Jj),"nares",False]
SyntaxError: invalid imaginary literal
X=[2,5.4,(6+9j),"nares",False]
X
[2, 5.4, (6+9j), 'nares', False]
type(x)
<class 'int'>
s = {22,4.4,8+4j,False,"nares'}
     
SyntaxError: unterminated string literal (detected at line 1)
s = {22,4.4,8+4j,False,'ares'}
     
s
     
{False, 'ares', 4.4, (8+4j), 22}
d={2:'naresh'}
     
d
     
{2: 'naresh'}
d={2:'nares','pavan':45,(3+6j,'356'}
   
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
d={2:'nares','pavan':45,(3+6j),'356'}
   
SyntaxError: ':' expected after dictionary key
d={2:'nares','pavan':45,(3+6j):'356'}
   
d
   
{2: 'nares', 'pavan': 45, (3+6j): '356'}
comples(10.8+0j)
   
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    comples(10.8+0j)
NameError: name 'comples' is not defined. Did you mean: 'complex'?
complex(10.8+0j)
   
(10.8+0j)
complex(False)
   
0j
complex(True)
   
(1+0j)
complex("nares?)
        
SyntaxError: unterminated string literal (detected at line 1)
comlex("nares")
        
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    comlex("nares")
NameError: name 'comlex' is not defined. Did you mean: 'complex'?
complex(True,False)
        
(1+0j)
complex(False,True)
        
1j
bool(10)
        
True
bool(0)
        
False
str(8+9j)
        
'(8+9j)'
range(0,3,54)
        
range(0, 3, 54)
l=[1,2,4,5]
        

print(l)
        
[1, 2, 4, 5]
l.remove()
        
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    l.remove()
TypeError: list.remove() takes exactly one argument (0 given)
print(l[2])
        
4

