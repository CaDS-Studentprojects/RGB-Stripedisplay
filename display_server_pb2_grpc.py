# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import display_server_pb2 as display__server__pb2


class WS2801_DisplayStub(object):
  """service definition
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.DISPLAY_CHANGE = channel.unary_unary(
        '/LED_display.WS2801_Display/DISPLAY_CHANGE',
        request_serializer=display__server__pb2.DISPLAY_MSG.SerializeToString,
        response_deserializer=display__server__pb2.DISPLAY_RESPONSE.FromString,
        )


class WS2801_DisplayServicer(object):
  """service definition
  """

  def DISPLAY_CHANGE(self, request, context):
    """Make RPC on function DISPLAY_CHANGE with message DISPLAY_MSG
    server response with DISPLAY_RESPONSE
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_WS2801_DisplayServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'DISPLAY_CHANGE': grpc.unary_unary_rpc_method_handler(
          servicer.DISPLAY_CHANGE,
          request_deserializer=display__server__pb2.DISPLAY_MSG.FromString,
          response_serializer=display__server__pb2.DISPLAY_RESPONSE.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'LED_display.WS2801_Display', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
