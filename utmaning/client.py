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

        if data.startswith("START"):
            symbol = data.split()[1]
            print(f"Du är spelare {symbol}")

        elif data == "YOUR_TURN":
            move = input("Din tur (0-8): ")
            client.sendall(move.encode())

        elif data.startswith("BOARD"):
            _, board = data.split(" ", 1)
            print_board(board)

        elif data.startswith("WIN"):
            winner = data.split()[1]
            print(f"Spelare {winner} vann!")
            break

        elif data == "DRAW":
            print("Oavgjort!")
            break

        elif data == "INVALID":
            print("Ogiltigt drag, försök igen!")

    client.close()