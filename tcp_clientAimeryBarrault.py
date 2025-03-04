import socket

def start_tcp_client():
    host = '127.0.0.1'
    port = 65432

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        print("Connected to the server!")
    except ConnectionRefusedError:
        print("Unable to connect to the server. Is it running?")
        return

    game_over = False

    while not game_over:
        try:
            # Receive the server's message
            message = client_socket.recv(1024).decode()
            if not message:
                print("Disconnected from the server.")
                break
            print("Server:", message)

            if "Your turn!" in message:
                # It's the client's turn to guess
                guess = input("Enter your guess: ")
                if not guess.isdigit():
                    print("Invalid input. Please enter a valid number.")
                    continue
                client_socket.sendall(guess.encode())
            elif "Winner" in message or "You lose" in message or "Game over" in message:
                game_over = True

        except ConnectionAbortedError:
            print("The server closed the connection unexpectedly.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

    client_socket.close()
    print("Disconnected from the server.")

if __name__ == "__main__":
    start_tcp_client()
