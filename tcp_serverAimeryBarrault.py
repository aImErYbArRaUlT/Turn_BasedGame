import socket
import random

def start_tcp_server():
    host = '127.0.0.1'
    port = 65432

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)
    print("Server is listening...")

    # Accept connections from two clients
    client_sockets = []
    for i in range(2):
        client_socket, addr = server_socket.accept()
        client_sockets.append(client_socket)
        print(f"Client {i+1} connected from {addr}")

    # Generate a random target number
    target_number = random.randint(1, 100)
    print("A random target number has been generated.")

    game_over = False
    turn = 0  # Start with Client 1 (turn alternates between 0 and 1)

    while not game_over:
        try:
            current_client = client_sockets[turn]
            other_client = client_sockets[1 - turn]

            # Notify the current client it's their turn
            current_client.sendall(b"Your turn! Guess a number between 1 and 100: ")
            other_client.sendall(b"Waiting for the other player to guess...\n")

            guess = current_client.recv(1024).decode().strip()
            print(f"Client {turn+1} guessed a number.")  # High-level output for server logs

            # Validate the guess
            if not guess.isdigit():
                current_client.sendall(b"Invalid input. Please enter a number.\n")
                continue  # Retry the same turn

            guess = int(guess)

            if guess < 1 or guess > 100:
                current_client.sendall(b"Out of range. Guess a number between 1 and 100.\n")
                continue  # Retry the same turn

            # Check the guess
            if guess == target_number:
                current_client.sendall(b"Winner! You found the number.\n")
                other_client.sendall(b"The other player has found the number first. You lose.\n")
                game_over = True
            elif guess < target_number:
                current_client.sendall(b"Too low! The number is higher.\n")
                other_client.sendall(b"The other player guessed too low. Your turn is next.\n")
            else:
                current_client.sendall(b"Too high! The number is lower.\n")
                other_client.sendall(b"The other player guessed too high. Your turn is next.\n")

            if not game_over:
                turn = 1 - turn  # Switch turns if the game is not over

        except ConnectionResetError:
            print(f"Client {turn+1} disconnected unexpectedly.")
            # Notify the remaining client about the disconnection
            other_client.sendall(b"The other player has disconnected. Game over.\n")
            game_over = True
            break

    # Ensure final messages are sent before closing connections
    try:
        for client_socket in client_sockets:
            if client_socket:  # Check if the socket is still open
                client_socket.sendall(b"Game over. Thank you for playing!\n")
    except Exception as e:
        print(f"Error while sending final messages: {e}")

    # Close connections after the game
    for client_socket in client_sockets:
        client_socket.close()
    server_socket.close()
    print("Server closed.")

if __name__ == "__main__":
    start_tcp_server()
