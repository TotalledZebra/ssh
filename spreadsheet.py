
class SpreadSheet:

    def __init__(self):
        self._cells = {}

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def evaluate(self, cell: str) -> int | str:
        value = self._cells.get(cell, '')
        if value.startswith("'") and value.endswith("'"):
            return value[1:-1]
        try:
            int_value = int(value)
            return int_value
        except ValueError:
            return "#Error"

