from __future__ import absolute_import
from __future__ import annotations

import argparse

from ws.web_service import WebService

if __name__ == "__main__":

    argParser = argparse.ArgumentParser(description="Engine WS")

    argParser.add_argument("-wh", "--host", default="0.0.0.0", type=str, help="Web service host")
    argParser.add_argument("-wp", "--port", default=8000, type=int, help="Web service port")

    args = argParser.parse_args()

    ws = WebService(host=args.host, port=args.port)
    try:
        ws.run()
    except KeyboardInterrupt:
        exit()
