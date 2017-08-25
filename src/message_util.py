#!/usr/bin/python

import grpc
import echo_pb2
from grpc.beta import implementations

import hexdump, binascii
import argparse

def w(filename):
  req = echo_pb2.EchoRequest(firstname='john', lastname='doe')
  msg = binascii.b2a_hex(req.SerializeToString())
  frame =  '00' + hex(len(msg)/2).lstrip("0x").zfill(8) + msg
  print 'Raw Encode: ' + frame
  f = open(filename, "wb+")
  f.write(binascii.a2b_hex(frame))
  f.close()

def r(filename):
  f = open(filename, "rb")
  wire_msg = binascii.b2a_hex(f.read())
  f.close()
  print 'Got wire_message: ' + wire_msg
  message_length = wire_msg[2:10]
  msg = wire_msg[10:10+int(message_length, 16)*2]
  r = echo_pb2.EchoReply()
  r.ParseFromString(binascii.a2b_hex(msg))
  print 'Proto Decode: ' + r.message
  

parser = argparse.ArgumentParser(description='gRPC message client')
parser.add_argument("mode", default='write')
parser.add_argument("filename")
args = parser.parse_args()

if (args.mode == 'write'):
  w(args.filename)
elif (args.mode == 'read'):
  r(args.filename)
