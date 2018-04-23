import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 20001)
# message = 'This is the message.  It will be repeated.'

while True:

    message = raw_input("\nWhat is the data?")

    # Send data
    print 'sending "%s"' % message
    sent = sock.sendto(message, server_address)

    # Receive response
    print 'waiting to receive'
    data, server = sock.recvfrom(4096)
    print 'received "%s"' % data   