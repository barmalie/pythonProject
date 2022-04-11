#views

from models import init_field, has_emty_cell, empty_symvol, size_filed
from conf import first_player, second_player


def main():
    field = init_field()
    print_field(field)

    current_player, next_player = first_player, second_player
    while True:
        player_step(current_player)
        print_field()
        if is_win(field):# check is win
            print_win_msg(current_player)
            break
        if not has_empty_cell(field):
            print_draw_msg()

        enemy_step(next_player)
        print_win_msg(next_player)
        print_field()
        if is_win(field):# check is win
            print_win_msg(current_player)
            break
        if not has_emty_cell(field):
            print_draw_msg()
            break
        # change player

# ход игрока
def player_step(player_symvol: str):
    while True:
    try:
        coord = int(input('введите ячейку для хода от 1 до 9: '))
    except ValueError
        print("вы ввели не целое число")
    if 1 <=coord<= 9:
        print("введите число от 1 до 9")
        continue
    if not 1 <=coord<= 9:
        print("введите число от 1 до 9")
        continue

    x = (coord - 1) // size_filed
    y = (coord - 1) % size_filed
    if not is_empty_cell(field, row_index =x, col_index = y):
    print("ячейка занята")
    set_cell(field,
             row_index = x,
             col_index = y,
             player_symvol = player_symvol)
    break


# ход противника
def enemy_step(player_symvol: str):# может быть либо человек либо бот
    player_step()

def print_field(field: list[list]) -> None:
    start_num = 1
    for i in range(len(field)):
        for j in range(len(field[1])):
            print_symvol = start_num if field[i][j] == empty_symvol else field[i][j]# пустой символ в противном случае пустая ячейка
            start_num += 1
            print(print_symvol, end =" ")
        print()
    print("-"*20)

def print_win_msg(player_symvol: str ) -> None
    print(f"выиграл игрок{player_symvol}")

def print_draw_msg():
    print("ничья")

if __name__ == "__main__":
    main()
