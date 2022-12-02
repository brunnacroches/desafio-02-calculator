from src.controllers.interface.calculator import CalculatorInterface
from main.http_types.http_request import HttpRequest
from main.http_types.http_response import HttpResponse

class ThirdCalculatorController(CalculatorInterface):

    def third(self, input: HttpRequest, numbers: any):
        lista_de_numeros = []
        somatorio = 0
        for numero_da_lista in lista_de_numeros:
            somatorio += numero_da_lista

        if somatorio > lista_de_numeros:
            print("Success")
        else:
             print("Error")

        print(input)
        return HttpResponse(status_code=200, body={"success": True, "value": numbers})