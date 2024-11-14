import socket 

def start_client(host='127.0.0.1', port=8080):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"connected to server at {host}:{port}")

        while True:
            user_input = input("Enter numbers in form separated by ','(or 'quit' to exit): ")
            if user_input.lower() == 'quit':
                break
            client_socket.sendall(user_input.encode())
            response = client_socket.recv(1024).decode()
            print(f"Sorted response: {response}")


if __name__ == "__main__":
    start_client()