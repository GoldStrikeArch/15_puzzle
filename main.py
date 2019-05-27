from board import Board
from pynput import keyboard


My_Board = Board()


def main():
    My_Board.randomize()
    My_Board.screen_refresh()
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


def on_press(key):
    #My_Board.screen_refresh()
    pass




def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

    elif key == keyboard.Key.up:
        My_Board.board, My_Board.empty_loc = My_Board.move_up(My_Board.board, My_Board.empty_loc)

    elif key == keyboard.Key.down:
        My_Board.board, My_Board.empty_loc = My_Board.move_down(My_Board.board, My_Board.empty_loc)

    elif key == keyboard.Key.left:
        My_Board.board, My_Board.empty_loc = My_Board.move_left(My_Board.board, My_Board.empty_loc)

    elif key == keyboard.Key.right:
        My_Board.board, My_Board.empty_loc = My_Board.move_right(My_Board.board, My_Board.empty_loc)

    elif key == keyboard.Key.shift:
        My_Board.solve()

    return My_Board.screen_refresh()


if __name__ == "__main__":
    main()