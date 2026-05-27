import sys

from .game import check_winner, format_board, is_full, make_move, new_board


def parse_move(text: str):
    try:
        r, c = text.strip().split(",")
        return int(r) - 1, int(c) - 1
    except Exception:
        return None


def main():
    board = new_board()
    current = "X"
    while True:
        print("\n" + format_board(board) + "\n")
        move = input(
            f"Гравець {current}, вкажіть хід (рядок,стовпець) 1-3 або "
            f"'q' для виходу: "
        ).strip()
        if move.lower() == "q":
            print("Гра завершена.")
            sys.exit(0)
        parsed = parse_move(move)
        if not parsed:
            print("Неправильний формат. Приклад: 1,3")
            continue
        r, c = parsed
        if r not in range(3) or c not in range(3):
            print("Координати мають бути від 1 до 3.")
            continue
        if not make_move(board, r, c, current):
            print("Клітинка зайнята. Спробуйте ще.")
            continue
        winner = check_winner(board)
        if winner:
            print("\n" + format_board(board) + "\n")
            print(f"Переможець: {winner}")
            break
        if is_full(board):
            print("\n" + format_board(board) + "\n")
            print("Нічия.")
            break
        current = "O" if current == "X" else "X"


if __name__ == "__main__":
    main()
