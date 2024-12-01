from typing import Dict, List
from flask import request as FlaskRequest

class Calculator2:
    """
    Segunda Calculadora
    
    * N numeros são enviados.
    * Todos esses N numeros são multiplicados por 11 e elevados a pontência de 0.95.
    * Por fim, é retirado o desvio padrão desses resultados e retornado o inverso desse valor (1/result).
    """
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        print(body)
        input_data = self.__validate_body(body)
        print(input_data)
        
    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("body mal formatado!")
        
        input_data = body["numbers"]
        return input_data