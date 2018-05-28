from ctype import *
import struct
import sys
import os

class UDP(structure):
    _fields_=[("sr",c_ushort),
              ("des_port",c_ushort),
              ("length",c_long),
              ("checks",c_long)
              ]


def __new__(self, socket_buffer = None):
    return self.from_buffer_copy(socket_buffer)



def __init__(self, socket_buffer= None):
    self.src_port=socket.inet_ntoa(struct.pack("@I",self.sr))
    self.dest_port=socket.inet_ntoa(struct.pack("@I",self.des_port))


print(ip.src_port)