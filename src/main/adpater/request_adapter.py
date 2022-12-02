# aqui ficará todas as importaçoes (flask etc)

from flask import request as FlaskRequest
from main.http_types.http_request import HttpRequest
from main.http_types.http_response import HttpResponse
from controllers.interface.calculator import CalculatorInterface


def request_adapter(request: FlaskRequest, calculator: CalculatorInterface) -> HttpResponse:
  http_request = HttpRequest(
    header=request.headers,
    body=request.json,
    query_params=dict(request.args),
    path_params=request.view_args,
    url=request.full_path,
    ipv4=request.remote_addr,
  )

  http_response = calculator.calculate(http_request)
  return http_response