"""The Python implementation of the GRPC freedback client."""

from __future__ import print_function

import grpc

import freedback_pb2
import freedback_pb2_grpc


def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = freedback_pb2_grpc.ReceiverStub(channel)
  response = stub.submit(freedback_pb2.Entry(subject='you'))
  print("Greeter client received: " + response.url)

if __name__ == '__main__':
  run()
