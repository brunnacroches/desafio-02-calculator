from src.controllers.interface.calculator import CalculatorInterface
from main.http_types.http_request import HttpRequest
from main.http_types.http_response import HttpResponse

class SecondCalculatorController(CalculatorInterface):

    def second(self, numbers: any, input: HttpRequest) -> HttpResponse:
        lista_de_numeros = []
        for element in numbers:
            lista_de_numeros.append(element * 11) ** 0.95

        somatorio = 0
        for numero_da_lista in lista_de_numeros:
            somatorio += numero_da_lista

        somatorio = somatorio / 1000
        
        print(input)
        return HttpResponse(status_code=200, body={"success": True, "value": numbers})