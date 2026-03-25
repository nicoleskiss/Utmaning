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

    