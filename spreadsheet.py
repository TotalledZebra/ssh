
class SpreadSheet:
    def __init__(self):
        self._cells = {}
        self._evaluating = set()

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def evaluate(self, cell: str) -> int | str:
        if cell in self._evaluating:
            return "#Circular"
        self._evaluating.add(cell)
        
        value = self._cells.get(cell, '')
        if value.startswith("="):
            if value.startswith("='") and value.endswith("'"):
                result = value[2:-1]
            elif value[1:].isnumeric():
                result = int(value[1:])
            elif any(op in value for op in "+-*/"):
                try:
                    # Evaluate the arithmetic expression safely
                    result = eval(value[1:])
                    if isinstance(result, float) and not result.is_integer():
                        result = "#Error"
                    else:
                        result = int(result)
                except:
                    result = "#Error"
            else:
                ref = value[1:]
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
        
        self._evaluating.remove(cell)
        return result

