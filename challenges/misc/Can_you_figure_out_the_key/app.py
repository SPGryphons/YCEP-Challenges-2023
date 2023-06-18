import threading
from string import ascii_lowercase
from random import choices
from hashlib import md5
import socket


def sign(message, key):
    """ Our new keyed-hash message authentication algorithm! So much more simpler than HMAC! """
    return md5((key + message).encode()).hexdigest()


def verify(signed, key):
    """ Verifies if message is signed by key """
    try:
        message, signature = signed.split(".")
        return sign(message, key) == signature
    except:
        return False


def handle_client(client_socket, key):
    """ Handles a single client connection """
    PASSPHRASE = "Better than HMAC!"

    # Send welcome message to the user
    client_socket.sendall(b"Welcome to our new signing service!\n")
    client_socket.sendall(
        b"Our service is extremely secure, feel free to try and break it >:D\n")

    while True:
        # Send options to the user
        client_socket.sendall(b"\nOptions:\n")
        client_socket.sendall(b"1. Sign messages\n")
        client_socket.sendall(b"2. Verify messages\n")
        client_socket.sendall(b"3. Exit\n")
        client_socket.sendall(b"Enter option: ")

        # Receive option from the user
        option = client_socket.recv(1024).decode().strip()

        if option == "1":
            # Ask user for message to sign
            client_socket.sendall(b"Enter message: ")
            message = client_socket.recv(1024).decode().strip()
            if message == PASSPHRASE:
                client_socket.sendall(
                    b"Indeed! Our new algorithm runs much faster than HMAC :)\n")
            elif message:
                signed = f"{message}.{sign(message, key)}"
                client_socket.sendall(
                    f"Here's your signed message: {signed}\n".encode())
            else:
                client_socket.sendall(b"No message to sign\n")

        elif option == "2":
            # Ask user for signed message to verify
            client_socket.sendall(b"Enter signed message: ")
            signed = client_socket.recv(1024).decode().strip()
            if verify(signed, key):
                client_socket.sendall(b"Message verified!\n")
                try:
                    if signed.split(".")[0] == PASSPHRASE:
                        # Send flag to the client
                        with open("flag.txt") as f:
                            flag = f.read()
                            # Convert flag to bytes and send
                            client_socket.sendall(flag.encode())
                except:
                    client_socket.sendall(b"Flag is missing!\n")
            else:
                client_socket.sendall(b"Verification failed!\n")

        elif option == "3":
            client_socket.sendall(
                b"Goodbye! Thanks for using our service. Have a great day!\n")
            break
        else:
            client_socket.sendall(
                b"Invalid option. Please choose an option from 1 to 3!\n")

    # Close client socket
    client_socket.close()


def start_server():
    """ Starts the server and accepts client connections """
    # Create a socket for listening on port 7000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 7000))
    server_socket.listen(0)  # Allow unlimited connections

    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()

        # Generate a new key for each client connection
        key = ''.join(choices(ascii_lowercase, k=5))
        print(f"New client connected from {client_address[0]}. Key: {key}")

        # Start a new thread to handle the client connection
        threading.Thread(target=handle_client, args=(client_socket, key)).start()


start_server()
