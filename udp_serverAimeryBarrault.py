import socket
import random

def start_udp_server():
    host = '127.0.0.1'  # Localhost
    port = 65433  # Port for the server to listen on

    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))  # Bind to the specified host and port
    print("UDP Server is listening...")

    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    print(f"A random target number has been generated: {target_number}")

    clients = []  # To store client addresses
    game_over = False
    turn = 0  # Start with the first client (index 0)

    while not game_over:
        try:
            # Receive data from any client
            data, addr = server_socket.recvfrom(1024)
            message = data.decode().strip()

            if addr not in clients:
                if len(clients) < 2:
                    clients.append(addr)
                    server_socket.sendto(b"Welcome! Waiting for more players.\n", addr)
                    if len(clients) == 2:
                        server_socket.sendto(b"Game starting! You are Player 1.\n", clients[0])
                        server_socket.sendto(b"Game starting! You are Player 2.\n", clients[1])
                        server_socket.sendto(b"Your turn! Guess a number between 1 and 100:\n", clients[0])
                else:
                    server_socket.sendto(b"Game is full. Please wait for the next round.\n", addr)
                continue

            # Ensure only the current client can guess
            if addr == clients[turn]:
                guess = message
                print(f"Client {turn+1} guessed: {guess}")

                try:
                    guess = int(guess)
                    if guess == target_number:
                        server_socket.sendto(b"Winner! You found the number.\n", addr)
                        other_client = clients[1 - turn]
                        server_socket.sendto(b"The other player has found the number first. You lose.\n", other_client)
                        game_over = True
                    elif guess < target_number:
                        server_socket.sendto(b"Too low! The number is higher.\n", addr)
                        other_client = clients[1 - turn]
                        server_socket.sendto(b"The other player guessed too low. Your turn is next.\n", other_client)
                    else:
                        server_socket.sendto(b"Too high! The number is lower.\n", addr)
                        other_client = clients[1 - turn]
                        server_socket.sendto(b"The other player guessed too high. Your turn is next.\n", other_client)

                    if not game_over:
                        turn = 1 - turn  # Switch turn between 0 and 1
                except ValueError:
                    server_socket.sendto(b"Invalid input. Enter a valid number.\n", addr)
            else:
                server_socket.sendto(b"Not your turn. Wait for the other player.\n", addr)

        except Exception as e:
            print(f"An error occurred: {e}")
            break

    # Notify clients of the end of the game
    for client in clients:
        server_socket.sendto(b"Game over. Thank you for playing!\n", client)

    # Close the server socket
    server_socket.close()
    print("Server closed.")

if __name__ == "__main__":
    start_udp_server()
