import socket
import threading
from game_logic import TicTacToe

HOST = '0.0.0.0'
PORT = 65432

clients = []

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

        game.switch_player()
        current = 1 - current

    player1.close()
    player2.close()

def accept_clients():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("Server started... Waiting for players...")

    while True:
        conn, addr = server.accept()
        print(f"Player connected: {addr}")
        clients.append(conn)

        if len(clients) >= 2:
            p1 = clients.pop(0)
            p2 = clients.pop(0)
            threading.Thread(target=handle_game, args=(p1, p2)).start()

if __name__ == "__main__":
    accept_clients()