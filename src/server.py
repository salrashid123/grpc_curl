#!/usr/bin/python

import grpc
import echo_pb2
from grpc.beta import implementations

import time

_ONE_HOUR_IN_SECONDS = 60 * 60

class Greeter(echo_pb2.BetaEchoServerServicer):
  def SayHello(self, request, context):
    meta = dict(context.invocation_metadata())
    print 'Got RPC with message:  \n' + str(request)
    return echo_pb2.EchoReply(message='Hello, %s %s!' % (request.firstname, request.lastname ))

  def SayHelloStream(self, request, context):
    meta = dict(context.invocation_metadata())
    print 'Got RPC with message for Streaming :  \n' + str(request)
    yield echo_pb2.EchoReply(message='Streaming Hello 1, %s %s!' % (request.firstname, request.lastname ))
    yield echo_pb2.EchoReply(message='Streaming Hello 2, %s %s!' % (request.firstname, request.lastname ))
    return

keypairs = [(open('server_key.pem').read(),  open('server_crt.pem').read())]
sc = implementations.ssl_server_credentials(keypairs, open('CA_crt.pem').read(), False)
server = echo_pb2.beta_create_EchoServer_server(Greeter())

#server.add_insecure_port('[::]:50051')
server.add_secure_port('[::]:50051',server_credentials=sc)
server.start()
try:
  print 'Started gRPC server on port 50051'
  while True:
    time.sleep(_ONE_HOUR_IN_SECONDS)
except KeyboardInterrupt:
  server.stop()
