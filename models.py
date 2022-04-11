
from  conf import empty_symvol, size_filed
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
    return  False #func test


def is_win(field: list[list]) -> bool:
    win_combinations =[
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],

        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],

        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]

    ]
    for win_comb in win_combinations:
        cell_1 = get_cell(field,
                          cell_1_coord[0], cell_1_coord[1])
        cell_2 = get_cell(field,
                          cell_2_coord[0], cell_2_coord[1])
        cell_3 = get_cell(field,
                          cell_3_coord[0], cell_3_coord[1])
        if cell_1 == cell_2 == cell_3 != empty_symvol:
            return  True
    return False
        #cell_1_coord, cell_2_coord, cell_3_coord = win_comb

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
     field[row_index][col_index] == player_symvol
    #return field[row_index][col_index] == player_symvol
def test_empty_field():
     empty_field = init_field()
     assert is_win(empty_field) == False

 if _name__ == "__main__":
    test_field = init_field()
    print(test_field)


    assert is_win(test_field) == False
