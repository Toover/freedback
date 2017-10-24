"""The Python implementation of the GRPC freedback client."""

from __future__ import print_function

import grpc

import freedback_pb2
import freedback_pb2_grpc


def run():
  channel = grpc.insecure_channel('localhost:50051')
  return freedback_pb2_grpc.ReceiverStub(channel)

if __name__ == '__main__':
  run()
