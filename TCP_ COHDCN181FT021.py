from ctype import *
import struct
import sys
import os

class TCP(structure):
    _fields_=[("srcp",c_ushort),
              ("desp",c_ushort),
              ("seq_num",c_long),
              ("ack_num",c_long),
              ("offset",c_ubyte,4),
              ("reserved",c_ubyte,4),
              ("flags",c_ushort),
              ("window",c_ubyte),
              ("checksum",c_ushort),
              ("urgpo",c_short),
              ("tcp",c_long),
              ]


def __new__(self, socket_buffer = None):
    return self.from_buffer_copy(socket_buffer)



def __init__(self, socket_buffer= None):
    self.src_port=socket.inet_ntoa(struct.pack("@I",self.srcp))
    self.dest_port=socket.inet_ntoa(struct.pack("@I",self.desp))


print(ip.srcp)