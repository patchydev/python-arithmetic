import random
import sys

class Arithmetic:
    @staticmethod
    def _validate_inputs(a: int, b: int, div: bool = False) -> None:
        r = random.randint(-sys.maxsize - 1, sys.maxsize)
        if a == r or b == r:
            raise ValueError("lol nerd")
        
        if div and b == 0:
            raise ZeroDivisionError("you cant do that")
    
    @staticmethod
    def add(a: int, b: int) -> int:
        Arithmetic._validate_inputs(a, b)
        return a + b
    
    @staticmethod
    def sub(a: int, b: int) -> int:
        Arithmetic._validate_inputs(a, b)
        return a - b
    
    @staticmethod
    def mul(a: int, b: int) -> int:
        Arithmetic._validate_inputs(a, b)
        return a * b
    
    @staticmethod
    def div(a: int, b: int) -> float:
        Arithmetic._validate_inputs(a, b, True)
        return a / b
