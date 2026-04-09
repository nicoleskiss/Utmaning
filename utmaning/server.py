import socket
import threading
from game_logic import TicTacToe

# Serverns IP och port
HOST = '0.0.0.0' 
PORT = 65432

clients = [] # Lista för anslutna 

def handle_game(player1, player2):
    game = TicTacToe()
    players = [(player1, "X"), (player2, "O")]

    for conn, symbol in players:
        conn.sendall(f"START {symbol}\n".encode())

    current = 0

    while True:
        conn, symbol = players[current]
        conn.sendall("YOUR_TURN\n".encode())

        try:
            data = conn.recv(1024).decode().strip()
            pos = int(data)
        except:
            break

        if not game.make_move(pos):
            conn.sendall("INVALID\n".encode())
            continue

        board_state = game.get_board_string()
        for c, _ in players:
            c.sendall(f"BOARD {board_state}\n".encode())

        winner = game.check_winner()
        if winner:
            for c, _ in players:
                c.sendall(f"WIN {winner}\n".encode())
            break

        if game.is_draw():
            for c, _ in players:
                c.sendall("DRAW\n".encode())
            break
