import socket
import array

def connect(server, port):
    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.connect ((server, port))
    return s

def read_in(s, delim=b'!\n'):
    buf = b''
    while not buf.endswith(delim):
        buf += s.recv(1)
    print(buf)

def read_data(s, delim=b'\n'):
    buf = b''
    count = 0
    list = []
    while not buf.endswith(delim):
        new = s.recv(1)
        buf += new
        count = count + 1
        print(count, new)
        print(format(ord(new), 'b'))
        list.append(format(ord(new), 'b'))
        print(list) 
    return list

if __name__=="__main__":
    PORT = 1228
    SERVER = '172.30.75.139' 

s = connect(SERVER, PORT)
read_in(s)
arr_bin = read_data(s)
print("got to this spot")
#take first 4, put together
binstr = arr_bin[0]+arr_bin[1]+arr_bin[2]+arr_bin[3]
#THIS IS PROBABLY WRONG
#ARE THE BITS INT HE RIGHT PLACE FOR CONVERSION? 

int1 = int(binstr, 2))
binstr2 = arr_bin[4]+arr_bin[5]+arr_bin[6]+arr_bin[7]
int2 = int(binstr2,2))
summy = int1 + int2





#grab data
#data = s.recv(64)
#res = ''.join(format(ord(i), 'b') for i in data)
#print(len(str(res)))

