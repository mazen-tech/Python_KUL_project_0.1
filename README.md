# Python Sorting Echo Server

A simple Python-based Echo Server that receives a comma-separated list of numbers, sorts them in ascending order, and returns the sorted result to the client.

## Features

- Accepts a comma-separated list of numbers from the client.
- Sorts the numbers in ascending order.
- Returns the sorted numbers to the client.
- Handles invalid input gracefully with error messages.

## How It Works

1. The server listens for incoming TCP connections on a specified IP and port.
2. Upon connection, the client sends a comma-separated string of numbers.
3. The server parses the input, sorts the numbers, and sends back the sorted list.
4. If the input is invalid, the server responds with an error message.

---

## Requirements

- Python 3.x

## Setup and Usage

### 1. Clone the Repository
```bash
git clone https://github.com/mazen-tech/Python_KUL_project_0.1.git
cd python-sorting-echo-server 
```

### 2. Run the server and client on diffrent terminals 
```bash
python3 server.py
```
![image](https://github.com/user-attachments/assets/a6d22116-25ab-42ab-8a62-868cd5b5116a)


```bash 
python3 client.py
```
![image](https://github.com/user-attachments/assets/5d7b144f-3f3e-41b9-8bb4-e0067b9a6813)
