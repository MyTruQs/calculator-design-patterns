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
        pass
        