import socket

def connect(server, port):
    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.connect ((server, port))
    return s

def read_until(s, delim=b':'):
    #read in the initial text
    buf = b''
    while not buf.endswith(delim):
        buf += s.recv(1)
    print(buf) 
    #separate out the first number
    data =  s.recv(2048)
    print("hex number provided: ", data)
    #convert hex to int
    idata = int(data.rstrip("\n"), 16)
    print("decimal calculated: ", idata)
    #s.sendall(str(idata))
    s.sendall(str(idata) + " \n")
    ndata = s.recv(2048)
    print(ndata)
    nndata = s.recv(2048)
    print(nndata)
    #neato line to grab int using list comprehension (converts string to list and itering through list)
    resdec = [int(i) for i in nndata.split() if i.isdigit()]
    print(bin(resdec[0]))
    s.sendall(str(bin(resdec[0]).replace("0b", "")) + " \n")
    nextynext = s.recv(2048)
    print(nextynext)
    buf = b''
    while not buf.endswith(delim):
        buf += s.recv(1)
    print(buf)
    nnextynext = s.recv(18)
    dataprep = nnextynext.strip().split(" ")
    print(dataprep)
    prodd = int(dataprep[0], 16) * int(dataprep[1], 16)
    print("product: ", prodd)
    #convert to 32 bit
    binit = int(bin(prodd+2**32)[-32:])
    print(binit)
    print(len(str(binit)))
    hexit = hex(int(str(binit),2))
    moar = s.recv(2048)
    print(moar)
    s.sendall(str(hexit) + " \n") 
    isitdone = s.recv(2048)
    print(isitdone) 
    waitwhyisntitover = s.recv(2048)
    print(waitwhyisntitover)

if __name__ == "__main__":
    PORT = 1392
    SERVER = '172.30.75.139'

s = connect(SERVER,PORT)
read_until(s)

        
