import socket


if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('172.17.30.81', 4000))
    print("Connnected")
    while True:
        # get user input for message to send
        message = ("Enter message: ")

        # send the message to the server
        client_socket.send(message.encode('utf-8'))

        # receive the response from the server
        data = client_socket.recv(1024)

        # print the response
        print(f"Received response: {data.decode('utf-8')}")
    client_socket.close()

