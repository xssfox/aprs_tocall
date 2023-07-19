from . import Parser
import argparse
import sys

def main():
    cli = argparse.ArgumentParser(
                    prog='aprs_tocall',
                    description='Looks up APRS tocalls')
    cli.add_argument('tocall', type=str, help="The APRS tocall to lookup")  
    cli.add_argument('--online', help="Use online rather than distributed version",
                    action='store_true', default=False)
    args = cli.parse_args()
    aprs_tocall = Parser(offline=not args.online)
    
    try:
        data = aprs_tocall.lookup(args.tocall)
        for key in data:
            print(f"{key}={data[key]}")
    except IndexError:
        sys.stderr.write("Could not find call in tocalls.yaml\n")
if __name__ == '__main__':
    main()