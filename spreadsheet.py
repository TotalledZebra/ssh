import re

from test_pycosat import evaluate


class SpreadSheet:
    def __init__(self):
        self._cells = {}
        self._evaluating = set()

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def evaluate(self, cell: str) -> int | str:

        cell_pattern = re.compile("[A-Z]+[1-9]+")

        value = self._cells.get(cell, '')

        if cell in value:
            return "#Circular"

        # Handle formula
        if value.startswith("="):

            expression = value[1:]

            # Handle strings
            if value.startswith("'") and value.endswith("'"):
                result = expression[1:-1]

            # Handle numeric values
            elif expression.isnumeric():
                result = int(expression)

            elif any(op in expression for op in "+-*/"):

                try:

                    # Split the expression into tokens and find any potential circular references
                    tokens = re.split("[+\\-*/]", expression)

                    for token in tokens:
                        if cell_pattern.match(token) and cell in self._cells.get(token):
                            return "#Circular"

                    # AI generated part, replace references with their values
                    for ref in self._cells:
                        if ref in expression:
                            ref_value = self.evaluate(ref)
                            if isinstance(ref_value, int):
                                expression = expression.replace(ref, str(ref_value))
                            else:
                                return "#Error"

                    result = eval(expression)

                    if isinstance(result, float) and not result.is_integer():
                        result = "#Error"
                    else:
                        result = int(result)
                except:
                    result = "#Error"
            else:
                ref = expression
                if ref in self._cells:
                    result = self.evaluate(ref)
                else:
                    result = "#Error"
        elif value.startswith("'") and value.endswith("'"):
            result = value[1:-1]
        else:
            try:
                result = int(value)
            except ValueError:
                result = "#Error"

        return result

