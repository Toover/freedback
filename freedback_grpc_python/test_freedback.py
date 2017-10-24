import freedback_pb2
import freedback_server
import freedback_client
import time

if __name__ == '__main__':
  server = freedback_server.serve()
  client = freedback_client.run()
  response = client.submit(freedback_pb2.Entry(subject='you'))
  print("Greeter client received: " + response.url)
  server.stop(0)
