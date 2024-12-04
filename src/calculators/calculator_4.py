from typing import Dict, List
from flask import request as FlaskRequest
from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator4:
    """
    Quarta Calculadora
    
    * N números são colocados como entrada.
    * Retornar a média dos números. 
    """
        
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        
        average = self.__calculate_average(input_data)
        
        formated_response = self.__format_response(average)
        return formated_response
    
    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado!")
        
        input_data = body["numbers"]
        return input_data
    
    def __calculate_average(self, numbers: List[float]) -> float:
        return sum(numbers) / len(numbers)
        
    def __format_response(self, average: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "average": round(average, 2)
            }
        }