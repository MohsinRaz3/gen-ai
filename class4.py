""" from typing import Any  

fruits: list[str] = ["saib", "angoor", "anaar","kharboza"]
print(f'my favourite phaal is {fruits[3]}')
"""
from typing import Tuple,Dict

def my_function(a:int,b:int, *abc:int, **xyz:int):
    print(f"1st param: {a},\n2nd param: {b}, \n3rd Argumenets {abc}, \n4th All positional args  {xyz}")
    
my_function(1,3,4,5,6,7,8, d=3,f=5)