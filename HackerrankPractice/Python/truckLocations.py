# WIP - Incomplete

# Truck locations 
# Python program 

# A logistics company has a central software solution to track the position of their trucks
# Different applications are interested in different trucks
# To save bandwidth the company wants to have a central subscriber for each local office 
# This service will then be used by the applications in the office to get position updates 

# Your task is to implement the subscriber class 
# The subscriber can request information form the central server by providing the ID for a truck 
# The server will return the current position and will afterwards send position updates as differences as they become available 

# When a client subscribes to a truck the subscriber should return the current truck position 
# Additionally the client can request an update 
# In that case the client should receive all the updates for all trucks since it last requested an update
# It is important that all updates arrive in the same order as they were initially sent out
# Truck positions are represented in x and y coordinates 
# have a look at the provided source code to understand which inputs are provided and which outputs are expected for the Subscriber class 

# Also be aware that you can call the SubscribeToTruck function of the IServer interface
# If you want to define custome test cases or understand the provided test cases the following definitions might help you 
# The input format is defined as follows 
# The first row contains one number N for the number of trucks
# the next N rows contain the initial coordinates of the trucks as two space-separated numbers X_i and Y_i
# The remaining (arbitrary number of) rows each contain one of three possible commands 
# S<ClientId><TruckId>means that client with id ClientId subscribes to the truck with ID TruckId 
# U<TruckId><delta_x><delta_y> means that truck with id TruckId moved by delta_x delta_y coordinates 
# R<ClientId> means that the Client with ID CliendId requests position updates 

# The output format is defined as follows 
# Clients print the answer they get as an subscription request like this 
# S<ClientId><TruckId><x_pos><y_pos> 
# Clients prints all updates they get as 
# U<ClientId><TruckId><delta_x><delta_y> 

# Example 
# Consider the following example input 
# 1
# 2 3
# U 0 1.5 2.5 
# S 0 0 
# U o 1 2 
# U 0 -0.5 -0.5
# S 1 0 
# R 0 
# U 0 1 1
# R 1

# This should produce the following output 
# S 0 0 2.5 5.5 
# S 1 0 4 7
# U 0 1 2 
# U 0 -0.5 -0.5
# U 1 1 1 

# Explanation
# The first line of output is produced when client with ID = 0 subscribes to truck with ID=0
# At that point truck with ID=0 is at (3.5, 5.5) 

# The second line of output is produced when the client with ID=1 subscribes to truck with ID=0
# At that point the truck is at (4, 7) 

# The third and fourth line of output are produced when the client with ID=0 requests position updates for truck with ID=0
# Since there were 2 updates after the subscription, there's one line for each update 

# The fifth line of output is produced when client with ID=1 requests position updates for truck with ID=0
# Since there was 1 update after the subscription, there's one line of output 

from dataclasses import dataclass, replace

# 
@dataclass
class TruckPosition:
    x: float
    y: float

# 
@dataclass
class TruckPositionDelta:

    #
    truck_id: int
    
    #
    delta_x: float
    
    #
    delta_y: float


class Subscriber:
    def __init__(self, server):
        self.server = server
        self.subscriptions = {}  # {client_id: {truck_id: TruckPosition}}

    def process_update(self, update):
        # Store the update for the specified truck and client
        client_id = update.truck_id
        truck_id = update.truck_id
        delta_x = update.delta_x
        delta_y = update.delta_y

        if client_id not in self.subscriptions:
            self.subscriptions[client_id] = {}
        if truck_id not in self.subscriptions[client_id]:
            self.subscriptions[client_id][truck_id] = TruckPosition(0, 0)

        self.subscriptions[client_id][truck_id].x += delta_x
        self.subscriptions[client_id][truck_id].y += delta_y

    def subscribe_to_truck(self, truck_id, client_id):
        # Subscribe to a truck and return its current position
        pos = self.server.subscribe_to_truck(truck_id)
        if client_id not in self.subscriptions:
            self.subscriptions[client_id] = {}
        self.subscriptions[client_id][truck_id] = pos
        return pos

    def get_updates(self, client_id):
        # Get all updates for a specific client since the last update request
        updates = []

        if client_id in self.subscriptions:
            for truck_id in self.subscriptions[client_id]:
                pos = self.subscriptions[client_id][truck_id]
                updates.append(TruckPositionDelta(truck_id, pos.x, pos.y))

        return updates


class Server:
    def __init__(self):
        self.registered_trucks = set()
        self.current_pos = {}

    def subscribe_to_truck(self, truck_id):
        self.registered_trucks.add(truck_id)
        return replace(self.current_pos[truck_id])

    def add_position(self, truck_id, pos):
        self.current_pos[truck_id] = pos

    def on_update(self, subscriber, delta):
        if delta.truck_id in self.registered_trucks:
            subscriber.process_update(delta)
        pos = self.current_pos[delta.truck_id]
        pos.x += delta.delta_x
        pos.y += delta.delta_y


class Client:
    def __init__(self, client_id, subscriber):
        self.client_id = client_id
        self.subscriber = subscriber

    def subscribe(self, truck_id):
        pos = self.subscriber.subscribe_to_truck(truck_id, self.client_id)
        print(f"S {self.client_id} {truck_id} {pos.x:g} {pos.y:g}")

    def request_update(self):
        updates = self.subscriber.get_updates(self.client_id)
        for delta in updates:
            print(f"U {self.client_id} {delta.truck_id} {delta.delta_x:g} {delta.delta_y:g}")

def main():
    server = Server()
    subscriber = Subscriber(server)

    # Sample input
    input_lines = [
        "1",
        "2 3",
        "U 0 1.5 2.5",
        "S 0 0",
        "U 0 1 2",
        "U 0 -0.5 -0.5",
        "S 1 0",
        "R 0",
        "U 0 1 1",
        "R 1"
    ]

    current_line = 0

    def read_line():
        nonlocal current_line
        current_line += 1
        return input_lines[current_line - 1].split()

    num_trucks = int(read_line()[0])
    for i in range(num_trucks):
        line = read_line()
        x = float(line[0])
        y = float(line[1])
        server.add_position(i, TruckPosition(x, y))

    while current_line < len(input_lines):
        line = read_line()
        if len(line) == 0:
            break
        elif line[0] == "S":
            client_id = int(line[1])
            truck_id = int(line[2])
            subscriber.subscribe_to_truck(truck_id, client_id)
        elif line[0] == "U":
            truck_id = int(line[1])
            dx = float(line[2])
            dy = float(line[3])
            server.on_update(subscriber, TruckPositionDelta(truck_id, dx, dy))
        elif line[0] == "R":
            client_id = int(line[1])
            updates = subscriber.get_updates(client_id)
            for delta in updates:
                print(f"U {client_id} {delta.truck_id} {delta.delta_x:g} {delta.delta_y:g}")
        else:
            raise Exception("Invalid input")

if __name__ == "__main__":
    main()
    # read_line = lambda: sys.stdin.readline().split()

    # server = Server()
    # subscriber = Subscriber(server)
    # clients = []

    # num_trucks = int(read_line()[0])
    # for i in range(num_trucks):
    #     line = read_line()
    #     x = float(line[0])
    #     y = float(line[1])
    #     server.add_position(i, TruckPosition(x, y))

    # while True:
    #     line = read_line()
    #     if len(line) == 0:
    #         break
    #     elif line[0] == "S":
    #         client_id = int(line[1])
    #         truck_id = int(line[2])
    #         if client_id >= len(clients):
    #             clients.append(Client(client_id, subscriber))
    #         clients[client_id].subscribe(truck_id)
    #     elif line[0] == "U":
    #         truck_id = int(line[1])
    #         dx = float(line[2])
    #         dy = float(line[3])
    #         server.on_update(subscriber, TruckPositionDelta(truck_id, dx, dy))
    #     elif line[0] == "R":
    #         client_id = int(line[1])
    #         clients[client_id].request_update()
    #     else:
    #         raise Exception("Invalid input")
