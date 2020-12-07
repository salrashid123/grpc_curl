#!/usr/bin/python

import grpc
import echo_pb2
import echo_pb2_grpc

import argparse

def run(host,port):
  _TIMEOUT_SECONDS = 1
 
  cc =  grpc.ssl_channel_credentials(open('CA_crt.pem', 'rb').read())
  channel = grpc.secure_channel('{}:{}'.format(host, port), cc)
  #channel = grpc.insecure_channel(host,port)
  stub = echo_pb2_grpc.EchoServerStub(channel)
  response = stub.SayHello(echo_pb2.EchoRequest(firstname='john', lastname='doe'), _TIMEOUT_SECONDS)
  print(response)

  #response = stub.SayHelloStream(echo_pb2.EchoRequest(firstname='john', lastname='doe'), _TIMEOUT_SECONDS)
  #for msg in response:
  #  print msg

parser = argparse.ArgumentParser(description='gRPC client')
parser.add_argument("host", default='server.domain.com')
parser.add_argument("port", default=50051, type=int)
args = parser.parse_args()
run(args.host, args.port)