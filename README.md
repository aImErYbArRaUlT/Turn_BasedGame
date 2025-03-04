Turn-Based Multiplayer Number Guessing Game

Author: Aimery Barrault
Course: CSCI 340: Networking
Date: December 12th, 2024

Project Overview:
This project implements a turn-based multiplayer number guessing game using both TCP and UDP protocols. 
The game involves two players taking turns to guess a random number between 1 and 100. The server manages communication, player turns, feedback, and game results. 
The project showcases the differences between TCP and UDP in terms of reliability and connection handling.

How to Run the Code:

TCP Version:

Open a terminal and run the TCP server:
python tcp_serverAimeryBarrault.py

Open two separate terminals for the clients and run the TCP client script in each:
python tcp_clientAimeryBarrault.py

Follow the on-screen instructions to play the game. The server will alternate turns between the two players, provide feedback, and announce the winner.

UDP Version:

Open a terminal and run the UDP server:
python udp_serverAimeryBarrault.py

Open two separate terminals for the clients and run the UDP client script in each:
python udp_clientAimeryBarrault.py

Follow the on-screen instructions to play the game. The server will alternate turns, provide feedback, and announce the winner.

Dependencies:

Python Version: The code is compatible with Python 3.10 or later.
Libraries: Only the socket library is used, which is part of the Python standard library.
Game Features

Players take turns guessing a random number between 1 and 100.
The server provides feedback for each guess:
"Too high! The number is lower."
"Too low! The number is higher."
The server announces the winner and loser:
"Winner! You found the number."
"The other player has found the number first. You lose."
Both players receive a final message: "Game over. Thank you for playing."
Differences Between TCP and UDP

TCP Version:
Reliable communication with automatic error handling.
Maintains persistent connections between the server and clients.
Slower but ensures message delivery and order.
UDP Version:
Faster but requires additional logic to handle reliability.
Uses connectionless communication.
Clients must resend guesses if no response is received.
Common Issues and Fixes

Server Not Responding:

Ensure the server script is running before starting the clients.
Check that the correct host (127.0.0.1) and port (65433) are specified.
Timeouts in UDP Client:

If a client receives "No response from server," verify that the server is running and that the client is registered correctly.
Game Freezing:

Ensure both clients are connected before playing. The game requires exactly two players.
Invalid Input:

If a player enters a non-numeric guess or a number out of range, the server will ask them to try again.

File List:

tcp_serverAimeryBarrault.py: TCP server code.
tcp_clientAimeryBarrault.py: TCP client code.
udp_serverAimeryBarrault.py: UDP server code.
udp_clientAimeryBarrault.py: UDP client code.
README.md: This file contains instructions for running the project.
