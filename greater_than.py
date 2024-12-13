Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def greaterThan(x, y):
...     if x > y:
...         return True
...     else:
...         return False
... 
...     
>>> def main():
...     a = 2
...     b = 3
...     result = greaterThan(a, b)
...     print("The statement", str(a), "is greater than", str(b), "is", str(result))
... 
...     
>>> a = 10
>>> b = 6
>>> result = greaterThan(a, b)
>>> print("The statement", str(a), "is greater than", str(b), "is", str(result))
The statement 10 is greater than 6 is True
>>> a = 2
>>> b = 3
>>> result = greaterThan(a, b)
>>> print("The statement", str(a), "is greater than", str(b), "is", str(result))
The statement 2 is greater than 3 is False
