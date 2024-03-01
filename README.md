# pycparser-stubs
Type information for `pycparser`.  

## warning
This typing stub package is mainly written according to [C language section of cppreference.com](https://en.cppreference.com/w/c/language) and runtime tests, so there can be wrong annotations.  
Also, I haven't tested it with mypy, but it is usable with Pylance.  

## type alias
All type alias only exist in this package and **is not avaliable at runtime**. Put them in quotes if you want you use them to annotate. For example:  
```python
from pycparser import c_ast

def get_decl_name(decl: 'c_ast.Declarator') -> str:
    while type(decl) != c_ast.TypeDecl:
        decl = decl.type
    return decl.declname or ''
```
Without quotes you will get:  
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'pycparser.c_ast' has no attribute 'Declarator'
```
