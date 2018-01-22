import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5027
    
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    num, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    num2 = int(num) # change type of variable from string to integer
    
    
    def fac(n):  # factorial function
      num2 = 1
      while n >= 1:
        num2 = num2 * n
        n = n - 1
        return num2
      
      print "The Answer is ", fac(num2)

 


   


    
     

