#views

from models import init_field, has_emty_cell
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
        if not has_empty_cell(field)
            print_draw_msg

        enemy_step(next_player)
            print_win_msg(next_player)
        print_field()
            break
        if not has_emty_cell(field)
            print_draw_msg()
        # change player

# ход игрока
def player_step(player_symvol: str):
# ход противника
def enemy_step(player_symvol: str):# может быть либо человек либо бот
    player_step()

def print_field(field: list[list]) -> None:

def print_win_msg(player_symvol: )

def print_draw_msg():

if __name__ == "__main__":
    main()
