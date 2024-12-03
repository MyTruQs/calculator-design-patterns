from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator3:
    """
    Terceira Calculadora
    
    * N números são colocados como entrada.
    * Caso a variância de todos esses números for menor que a multiplicação deles, é apresentado uma informação de sucesso ao usuário.
    * Caso contrário, é apresentado uma informação de falha.
    """

    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler
        
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        
        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        self.__verify_results(variance, multiplication)
        
        formated_response = self.__format_response(variance)
        return formated_response
        
    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("body mal formatado!")
        
        input_data = body["numbers"]
        return input_data
    
    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handler.variance(numbers)
        return variance
    
    def __calculate_multiplication(self, numbers: List[float]) -> float:
        multiplication = 1
        for num in numbers: multiplication *= num
        return multiplication
    
    def __verify_results(self, variance: float, multiplication: float) -> None:
        if variance > multiplication:
            raise Exception("Fallha no processo: Variância maior que a multiplicação dos números.")
        
    def __format_response(self, variance: float) -> Dict:
        return {
            "data": {
                "Calculator": 3,
                "value": variance,
                "Success": True
            }
        }