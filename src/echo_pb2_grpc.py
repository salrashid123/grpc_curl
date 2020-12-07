# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import echo_pb2 as echo__pb2


class EchoServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/echo.EchoServer/SayHello',
                request_serializer=echo__pb2.EchoRequest.SerializeToString,
                response_deserializer=echo__pb2.EchoReply.FromString,
                )
        self.SayHelloStream = channel.unary_stream(
                '/echo.EchoServer/SayHelloStream',
                request_serializer=echo__pb2.EchoRequest.SerializeToString,
                response_deserializer=echo__pb2.EchoReply.FromString,
                )


class EchoServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SayHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHelloStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EchoServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=echo__pb2.EchoRequest.FromString,
                    response_serializer=echo__pb2.EchoReply.SerializeToString,
            ),
            'SayHelloStream': grpc.unary_stream_rpc_method_handler(
                    servicer.SayHelloStream,
                    request_deserializer=echo__pb2.EchoRequest.FromString,
                    response_serializer=echo__pb2.EchoReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'echo.EchoServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EchoServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/echo.EchoServer/SayHello',
            echo__pb2.EchoRequest.SerializeToString,
            echo__pb2.EchoReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHelloStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/echo.EchoServer/SayHelloStream',
            echo__pb2.EchoRequest.SerializeToString,
            echo__pb2.EchoReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
