import argparse
import sys


class ArgumentParser(argparse.ArgumentParser):
    def error(self, message: str):
        self.print_usage(sys.stderr)
        if message == "argument --delete: expected one argument":
            self.exit(2, "Error: Unable to remove: no index provided")
        else:
            self.exit(2, message)
