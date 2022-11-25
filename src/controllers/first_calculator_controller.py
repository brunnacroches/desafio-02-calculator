import math

# * Primeira Calculadora →
# Um numero de entrada é partilhado em 3 partes iguais.
# * number_parte = number / 3 

# A primeira parte é dividida por 4 e seu resultado somado a 7.
# Após isso, é tirado a raiz quadrada desse valor e multiplicado por uma constante
# de 0.257.
# * parte_1 = (number_parte / 4 + 7).math.sqrt * 0.257

# A segunda parte é elevada a potência de 2.121, dividida por 5 e somado a 1
# A terceira parte se mantem no mesmo valor.
# Por fim, é feita a soma desses 3 valores e entregado o resultado


class FirstCalculatorController:
    def first(self, number: any):
        number_parte = number / 3
        parte_1 = (number_parte / 4 + 7).math.sqrt * 0.257
        parte_2 = number_parte**2.121 / 5 + 1
        parte_3 = number_parte

        number == parte_1 + parte_2 + parte_3

        return {"success": True, "value": number}
