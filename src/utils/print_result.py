import time


def t(f, *args):
    """This Functions is used to roughly get the time it took to execute the functions"""
    s = time.perf_counter()
    f(*args)
    e = time.perf_counter()
    return str(e - s)[:5]


class CompareTableResult:
    """Class to compare results in a table format:\n
    +-----------------------+\n
    |   Table Comparison    |\n
    +-----------------------+\n
    | Column 01 | Column 02 |\n
    | row1 col1 | row1 col2 |\n
    | row2 col1 | row2 col2 |\n
    +-----------------------+\n
    """

    LEFT_RIGHT = "|"
    JUNCTION = "+"
    TOP_BOTTOM = "-"

    def __init__(self, title: str = "Results", columns: list[str] = [""]) -> None:
        self.title = title
        self.headers = columns
        self.table = []

    def __str__(self) -> str:
        return self.draw_table()

    def addRow(self, row: list[str]):
        expected = len(self.headers)
        actual = len(row)
        if expected != actual:
            raise IndexError(
                f"row and table size does not match.Expected row to have {expected} items. Found {actual}"
            )
        self.table.append(row)

    def get_width(self) -> list[int]:
        "return a list with the correct width per column, based on biggest text"
        return [len(x) for x in self.headers]

    def draw_table(self):
        widths = self.get_width()
        width_total = sum(widths) + (len(widths) - 1)

        title_top_bottom = (
            f"{self.JUNCTION}{self.TOP_BOTTOM * width_total}{self.JUNCTION}\n"
        )
        title = f"{title_top_bottom}{self.LEFT_RIGHT}{self.title: ^{width_total}}{self.LEFT_RIGHT}\n{title_top_bottom}"

        headers = f"{self.LEFT_RIGHT}"
        headers += "".join(list(map(lambda x: f"{x}{self.LEFT_RIGHT}", self.headers)))

        # TODO: Find a more elegant way to show this
        body = f""
        for row in self.table:
            body += f"\n{self.LEFT_RIGHT}"
            for idx, col in enumerate(row):
                body += f"{col: ^{widths[idx]}.{widths[idx]}}{self.LEFT_RIGHT}"
        bottom_line = f"\n{self.JUNCTION}{self.TOP_BOTTOM * width_total}{self.JUNCTION}"
        return title + headers + body + bottom_line


if __name__ == "__main__":
    x = CompareTableResult("Table Comparison", [" Column 01 ", " Column 02 "])
    x.addRow(["row1 col1", "row1 col2"])
    x.addRow(["row2 col1", "row2 col2"])
    print(x)
