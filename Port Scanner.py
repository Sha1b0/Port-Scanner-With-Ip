import socket
from datetime import datetime
Target=input("Enter your Ip Address:")
Time=(Target + str(datetime.now()))
print(Target + Time)
Upperport=int(input("UpperLimit of Port"))
Lowerport=int(input("LowerLimit of Port"))
try:
    for port in range(Upperport, Lowerport):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((Target, port))
        if result == 0:
            print(f"Port {port} is open")
except KeyboardInterrupt:
    print("Exiting Now")
except socket.gaierror:
    print("HOST IS INVALID")