from communication.clientsocket import ClientSocket


class Player:
    def __init__(self, client_socket):
        self.client_socket = ClientSocket(client_socket)
        # TODO: Move this into one of the threads
        self.user_name = self.client_socket.prompt("Please enter the user name you want to use: ")
        self.inventory = []
        # TODO: Start the threads

    def send_thread(self):
        pass

    def receive_thread(self):
        pass
