from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class BigOComplexity(Enum):
    CONSTANT = 'O(1)'
    LINEAR = 'O(N)'
    QUADRATIC = 'O(N^2)'
    LOGARITHMIC = 'O(logN)'
    LOG_LINEAR = 'O(NlogN)'
    CUBIC = 'O(n^3)'
    EXPONENTIAL = 'O(2^n)'
    FACTORIAL = 'O(n!)'
    
    


algorithms_dict = {
    'linear_search': BigOComplexity.LINEAR.value,
    'binary_search': BigOComplexity.LOGARITHMIC.value,
    'bubble_sort': BigOComplexity.QUADRATIC.value
}


class Algorithm(BaseModel):
    name: str
    description: str
    complexity: str
    is_done: bool = False
    creation: int = int( datetime.timestamp(datetime.now()))
    
    # ? explain this 
    class Config:
        use_enum_values = True 
    