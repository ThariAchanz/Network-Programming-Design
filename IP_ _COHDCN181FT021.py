from ctype import *
import struct
import sys
import os

class IP(structure):
    _Properties_=[("version",c_ubyte,4),
              ("headerlength",c_ubyte,4),
              ("tos",c_ubyte),
              ("len",c_ushort),
              ("id",c_ushort),
              ("offset",c_ushort),
              ("ttl",c_ubyte),
              ("proto",c_ubyte),
              ("checks",c_ushort),
              ("src",c_long),
              ("dest",c_long)
              ]


def __new__(self, socket_buffer = None):
    return self.from_buffer_copy(socket_buffer)



def __init__(self, socket_buffer= None):
    self.src_address=socket.inet_ntoa(struct.pack("@I",self.src))
    self.dest_address=socket.inet_ntoa(struct.pack("@I",self.dest))


print(self.src_address)