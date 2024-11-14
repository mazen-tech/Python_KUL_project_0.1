import socket

def sort_number(nums):
    try:
        num_list = list(map(int, nums.split(',')))
        num_list.sort()
        return ','.join(map(str, num_list))
    except ValueError:
        return "Error: Invalid input. NUMBERS ONLY (1,2,3,4...)"


def start_server(host='127.0.0.1', port=8080):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server is running on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024).decode()
                    if not data:
                        break
                    print(f"Received: {data}")
                    response = sort_number(data)
                    conn.sendall(response.encode())


if __name__ == "__main__":
    start_server()