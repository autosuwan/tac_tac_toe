import tkinter as tk

window = tk.Tk()
window.title("Tic Tac Toe")
window.geometry("400x400")

table = [[0 for _ in range(3)] for _ in range(3)]
buttons = []
p1 = 1
p2 = 2
current_player = {"value": p1}

start_frame = tk.Frame(window)
start_frame.pack(expand=True, fill="both")

def start_game():
    start_frame.pack_forget()
    game_frame.pack(expand=True, fill="both")

game_frame = tk.Frame(window)

start_label = tk.Label(start_frame, text="Welcome to Tic Tac Toe!", font=("Arial", 16))
start_label.pack(pady=20)
start_button = tk.Button(start_frame, text="Start Game", command=start_game)
start_button.pack()

turn_label = tk.Label(game_frame, text=f"Player {current_player['value']}'s Turn", font=("Arial", 16))
turn_label.pack(pady=10)

board_frame = tk.Frame(game_frame)
board_frame.pack(expand=True)

def check_winner(table):
    for row in table:
        if row[0] == row[1] == row[2] != 0:
            return row[0]
    for col in range(3):
        if table[0][col] == table[1][col] == table[2][col] != 0:
            return table[0][col]
    if table[0][0] == table[1][1] == table[2][2] != 0:
        return table[0][0]
    if table[0][2] == table[1][1] == table[2][0] != 0:
        return table[0][2]
    return 0


def tic_tac_toe(p1, p2, table):
    def on_click(i, j):
        if table[i][j] == 0:
            table[i][j] = p1
            buttons[i][j].config(text="X" if p1 == 1 else "O", state="disabled")

            winner = check_winner(table)
            if winner != 0:
                turn_label.config(text=f"Player {winner} wins!")
                for x in range(3):
                    for y in range(3):
                        buttons[x][y].config(state="disabled")
                return

            if all(table[x][y] != 0 for x in range(3) for y in range(3)):
                turn_label.config(text="Draw!")
                return

            current_player["value"] = p2
            turn_label.config(text=f"Player {current_player['value']}'s Turn")
            for x in range(3):
                for y in range(3):
                    if table[x][y] == 0:
                        buttons[x][y].config(command=lambda i=x, j=y: tic_tac_toe(p2, p1, table)(i, j))
    return on_click


for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(board_frame, text="", width=10, height=4)
        btn.config(command=lambda i=i, j=j: tic_tac_toe(p1, p2, table)(i, j))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

window.mainloop()
