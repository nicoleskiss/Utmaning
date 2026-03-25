import socket

HOST = '127.0.0.1'  
PORT = 65432

# Skriver ut spelplanen 
def print_board(board):
    cells = board.split("|")
    print(f"""
 {cells[0]} | {cells[1]} | {cells[2]}
---+---+---
 {cells[3]} | {cells[4]} | {cells[5]}
---+---+---
 {cells[6]} | {cells[7]} | {cells[8]}
""")
    
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    symbol = ""

    while True:
        data = client.recv(1024).decode().strip()