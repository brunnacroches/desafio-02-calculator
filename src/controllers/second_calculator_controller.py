# * Segunda Calculadora → N numeros são colocados como entrada. Todos esses N numeros são
# multiplicados por 11 e elevados a potencia de 0.95. Por fim,
#  é realizada a soma de todos os numeros e realizado uma divisão por 1000
# e entregado o resultado

# LOOP


class SecondCalculatorController:
    def second(self, numbers: any):
        lista_de_numeros = []
        for element in numbers:
            lista_de_numeros.append(element * 11) ** 0.95

        somatorio = 0
        for numero_da_lista in lista_de_numeros:
            somatorio += numero_da_lista

        somatorio = somatorio / 1000

        return {"success": True, "value": numbers}

