empty_symvol ='_'
size_filed = 3
#созаем поле
def init_field(size:int = size_filed) -> list[list]:
    return [
        [empty_symvol for _ in range(size)]
        for _ in range(size)
    ]
print(init_field()) #тестирование

#проверяем поле на заполненость
def is_empty_cell(field: list[list],
                row_index: int,
                col_index: int) -> bool:
    return field[row_index][col_index] == empty_symvol


# ecть ли вопще пустая ячейка
def has_emty_cell(field: list[list]) -> bool:
    for row in field:
        for cell in row:
            if cell == empty_symvol:
                return  True
    return  False


def is_win(field: list[list]) -> bool:


# получить ячейку
def get_cell(field: list[list],
            row_index: int,
            col_index: int):
    return field[row_index][col_index]


# установить ячейку
def set_cell(field: list[list],
            row_index: int,
            col_index: int,
             player_symvol) -> None:
    return field[row_index][col_index] == player_symvol
