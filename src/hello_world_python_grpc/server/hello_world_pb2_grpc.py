# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from hello_world_python_grpc.server import hello_world_pb2 as hello__world__pb2


class HelloWorldGreeterStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SayHello = channel.unary_unary(
        '/hello_world.HelloWorldGreeter/SayHello',
        request_serializer=hello__world__pb2.HelloWorldRequest.SerializeToString,
        response_deserializer=hello__world__pb2.HelloWorldResponse.FromString,
        )


class HelloWorldGreeterServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SayHello(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_HelloWorldGreeterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SayHello': grpc.unary_unary_rpc_method_handler(
          servicer.SayHello,
          request_deserializer=hello__world__pb2.HelloWorldRequest.FromString,
          response_serializer=hello__world__pb2.HelloWorldResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'hello_world.HelloWorldGreeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
