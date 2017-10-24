"""The Python implementation of the GRPC freedback.Receiver."""

import time
from concurrent import futures
import grpc
import freedback_pb2
import freedback_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Receiver(freedback_pb2_grpc.ReceiverServicer):

  entries = dict()
  index = 0

  def Receiver(self):
    freedback_pb2_grpc.ReceiverServicer.__init__(self)

  def submit(self, entry, context):
    self.index = self.index + 1
    self.entries[self.index] = entry
    return freedback_pb2.EntryAccess(url=str(self.index), authentication='secret')

  def delete(self, entry_access, context):
    if entry_access.authentication == 'secret':
      del self.entries[int(entry_access.url)]
      return freedback_pb2.Empty()
    else:
      raise RuntimeException('invalid secret')

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  freedback_pb2_grpc.add_ReceiverServicer_to_server(Receiver(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  return server

if __name__ == '__main__':
  server = serve()
  try:
    while True:
      time.sleep(60 * 60 * 24)
  except KeyboardInterrupt:
    server.stop(0)
