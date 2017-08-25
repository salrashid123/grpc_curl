#!/usr/bin/python

import grpc
import echo_pb2
from grpc.beta import implementations

import argparse

def run(host,port):
  _TIMEOUT_SECONDS = 1
 
  cc = ssl_credentials = grpc.ssl_channel_credentials(open('CA_crt.pem').read())
  channel = implementations.secure_channel(host,port, cc)
  #channel = implementations.insecure_channel(host,port)
  stub = echo_pb2.beta_create_EchoServer_stub(channel)
  response = stub.SayHello(echo_pb2.EchoRequest(firstname='john', lastname='doe'), _TIMEOUT_SECONDS)
  print response

  #response = stub.SayHelloStream(echo_pb2.EchoRequest(firstname='john', lastname='doe'), _TIMEOUT_SECONDS)
  #for msg in response:
  #  print msg

parser = argparse.ArgumentParser(description='gRPC client')
parser.add_argument("host", default='main.esodemoapp2.com')
parser.add_argument("port", default=50051, type=int)
args = parser.parse_args()
run(args.host, args.port)