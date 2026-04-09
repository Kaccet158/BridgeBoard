#!/usr/bin/python3
import argparse
import sys
from .commands import cmd_login_dev, cmd_send, cmd_get, cmd_init_setup

def main():
    parser = argparse.ArgumentParser(description="CloudBridge CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("login", help="Open configuration file")
    subparsers.add_parser("send", help="Send current clipboard to cloud")
    subparsers.add_parser("get", help="Get clipboard from cloud")

    args = parser.parADMEse_args()

    if args.command == "login":
        cmd_init_setup()
    elif args.command == "login dev":
        cmd_login_dev()
    elif args.command == "send":
        cmd_send()
    elif args.command == "get":
        cmd_get()
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()