# RGB-Stripedisplay
GRPC driven driver for a self made RGB-LED-stripe display


### Regenerate proto files on the system

type in the console:     
`python -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/display_server.proto`

This regenerate `display_server_pb2.py` und `display_server_pb2_grpc.py`. With these you can run the `display.py` as the server.
