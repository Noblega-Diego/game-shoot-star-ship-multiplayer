import socket
from typing import TypedDict

from server.entities import Player

op = TypedDict('OP', {'type': str})
UserType = TypedDict('UserType', {'id': int, 'conexion': socket.socket, 'player': Player | None, 'middlemessages': str,
                                  'confirm': bool})
Data = TypedDict('Data', {'OP': op, 'data': dict[str, any]})
