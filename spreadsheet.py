
class SpreadSheet:
    def __init__(self):
        self._cells = {}

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def evaluate(self, cell: str) -> int | str:
        value = self._cells.get(cell, '')
        if value.startswith("="):
            # Evaluate formula
            if value.startswith("='") and value.endswith("'"):
                return value[2:-1]
            try:
                # Evaluate as integer if possible
                return int(value[1:])
            except ValueError:
                return "#Error"
        elif value.startswith("'") and value.endswith("'"):
            # Return string without quotes
            return value[1:-1]
        try:
            # Try to convert directly to integer
            return int(value)
        except ValueError:
            # Not a valid integer
            return "#Error"

