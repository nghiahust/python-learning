import argparse
parser = argparse.ArgumentParser(description="""
Prints out the words passed in, capitalizes them if required and repeat them in as many lines as rquested.
""")
parser.add_argument("message", help="Messages to be echoed", nargs="+")