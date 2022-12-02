from src.controllers.interface.calculator import CalculatorInterface
from main.http_types.http_request import HttpRequest
from main.http_types.http_response import HttpResponse


class FirstCalculatorController(CalculatorInterface):
    def first(self, number: any, input: HttpRequest) -> HttpResponse:
        number_parte = number / 3
        parte_1 = (number_parte / 4 + 7).math.sqrt * 0.257
        parte_2 = number_parte**2.121 / 5 + 1
        parte_3 = number_parte

        number == parte_1 + parte_2 + parte_3

        print(input)
        return HttpResponse(status_code=200, body={"success": True, "value": number})