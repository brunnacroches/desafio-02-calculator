from flask import request, jsonify
from main.adpater.request_adapter import request_adapter
from controllers.calculators.first_calculator import FirstCalculatorController
from controllers.calculators.second_calculator import SecondCalculatorController
from controllers.calculators.third_calculator import ThirdCalculatorController

from .server import app

@app.route("/", methods=["POST"])
def calculator_function():
  http_response = request_adapter(request, FirstCalculatorController(), SecondCalculatorController(), ThirdCalculatorController())
  return jsonify(http_response), http_response.status_code
