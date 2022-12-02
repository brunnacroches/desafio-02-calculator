from abc import ABC, abstractmethod
from main.http_types.http_request import HttpRequest
from main.http_types.http_response import HttpResponse


class FirstCalculatorController(ABC):

    @abstractmethod
    def first(self, number: any, input: HttpRequest) ->  HttpResponse:
        number_parte = number / 3
        parte_1 = (number_parte / 4 + 7).math.sqrt * 0.257
        parte_2 = number_parte**2.121 / 5 + 1
        parte_3 = number_parte

        number == parte_1 + parte_2 + parte_3

        return {"success": True, "value": number}


class SecondCalculatorController(ABC):

    @abstractmethod
    def second(self, input: HttpRequest, numbers: any)  ->  HttpResponse:
        lista_de_numeros = []
        for element in numbers:
            lista_de_numeros.append(element * 11) ** 0.95

        somatorio = 0
        for numero_da_lista in lista_de_numeros:
            somatorio += numero_da_lista

        somatorio = somatorio / 1000

        return {"success": True, "value": numbers}


class ThirdCalculatorController(ABC):

    @abstractmethod
    def third(self, input: HttpRequest, numbers: any) ->  HttpResponse:
        lista_de_numeros = []
        somatorio = 0
        for numero_da_lista in lista_de_numeros:
            somatorio += numero_da_lista

        if somatorio > lista_de_numeros:
            print("Success")
        else:
             print("Error")

        return {"success": True, "value": numbers}