import socket, time
from .commands import commands_0520

def reboot_psu(server_ip: str) -> bytes:
    """
    Reboot command is simply this sequence of 9-bytes commands sent via
    UDP to port 30704 with a 100ms delay in between the commands.
    """
    server_port: int = 30704
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.sendto(b'\x19\x04\x00\x00\x00\x04\x00\x00\x00', (server_ip, server_port))
        time.sleep(0.1)
        sock.sendto(b'\x1A\x04\x00\x00\x00\x00\x00\x00\x00', (server_ip, server_port))
        time.sleep(0.1)
        sock.sendto(b'\x1B\x04\x00\x00\x00\x00\x00\x00\x00', (server_ip, server_port))
        time.sleep(0.1)
        sock.sendto(b'\x1B\x04\x00\x00\x00\x04\x00\x00\x00', (server_ip, server_port))
        data, server = sock.recvfrom(4096)

    return data

class CaenEasyDriverControl:
    def __init__(self, server_ip: str, server_port: int):
        self.server_ip = server_ip
        self.server_port = server_port
        self.sock = None

    def __enter__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.server_ip, self.server_port))
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.sock is not None:
            self.sock.close()

    def send_command(self, command: str) -> bytes:
        """
        Send a command, and return the answer
        from a Caen Easy-Driver 0520. Maybe it works for other Caen PSUs?
        I dont know, havent tested it!

        The status register value can be directly read by users using the
        `MST\r` command. The returned item is a 2-digit hexadecimal ASCII
        string, corresponding to the equivalent status register. A brief
        description of all the binary flags is here presented:
        7: reserved
        6: reserved
        5: external interlock
        4: sunt temperature
        3: mosfet temperature
        2: dc undervoltage
        1: fault
        0: module on
        """
        if command not in commands_0520.keys():
            msg = f"'{command}' is not a valid command!"
            raise ValueError(msg)

        if command == "reboot":
            """
            The reboot command is different from the other commands since it
            is sent by UDP to port 30704.
            """
            return reboot_psu(server_ip=self.server_ip)

        self.sock.sendall((command + '\r').encode())
        response: bytes = self.sock.recv(4096)

        return response


if __name__ == "__main__":
    server_ip = '192.168.0.222' # Caen Easy-Driver 0520 dev
    server_port = 10001

    response: bytes = send_command(
        # command = "reboot",
        command = "MOFF",
        server_ip = server_ip,
        server_port = server_port
    )
    response: bytes = send_command(
        # command = "reboot",
        # command = "MOFF",
        command = "MST",
        server_ip = server_ip,
        server_port = server_port
    )

    print(commands_0520["MST"].response_mapper(response))