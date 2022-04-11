#views

from models import init_field, has_emty_cell, empty_symvol

first_player = "X"
second_player = "O"

def main():
    field = init_field()
    print_field(field)

    current_player, next_player =first_player, second_player
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
        # change player

# ход игрока
def player_step(player_symvol: str):
    try:
        str_coord = input('введите ячейку для хода от 1 до 9: ')
    except ValueError
        print("вы ввели не целое число")

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

def print_win_msg(player_symvol: )

def print_draw_msg():

if __name__ == "__main__":
    main()
