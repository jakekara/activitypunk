from argparse import _SubParsersAction


class Command:

    def __init__(self, subparsers:_SubParsersAction):
        self.parser = subparsers.add_parser(self.name, description=self.description)

    @staticmethod
    def main(args):
        raise Exception("Not implemented")

