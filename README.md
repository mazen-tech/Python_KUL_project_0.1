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
git clone https://github.com/your_username/python-sorting-echo-server.git
cd python-sorting-echo-server
