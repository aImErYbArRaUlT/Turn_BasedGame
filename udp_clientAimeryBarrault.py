import socket

def start_udp_client():
    host = '127.0.0.1'  # Server's IP address
    port = 65433  # Port to connect to

    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (host, port)

    game_over = False

    # Send initial message to register with the server
    client_socket.sendto(b"READY", server_address)

    while not game_over:
        try:
            # Wait for a prompt from the server
            client_socket.settimeout(5)  # Set a timeout for server responses
            data, _ = client_socket.recvfrom(1024)
            message = data.decode()
            print("Server:", message)

            if "Winner" in message or "Game over" in message or "lose" in message:
                game_over = True
            elif "Your turn" in message:
                # It's the client's turn to guess
                guess = input("Enter your guess: ")
                client_socket.sendto(guess.encode(), server_address)
        except socket.timeout:
            print("No response from server. Retrying...")
            continue
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

    # Close the client socket
    client_socket.close()
    print("Disconnected from the server.")

if __name__ == "__main__":
    start_udp_client()
