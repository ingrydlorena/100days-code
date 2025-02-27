'''
Day 83: Command-line tool
Create a command-line tool with argparse.
'''

import argparse

def main():
    parser = argparse.ArgumentParser(description='Exemple of a CLI tool')

    parser.add_argument('name', help='your name')
    parser.add_argument('--greet', action='store_true', help='Shows a personalized greeting')
    parser.add_argument('--beatiful', action='store_true', help='Shows how beatiful you are')

    args = parser.parse_args()
    args = parser.parse_args()

    if args.greet:
        print(f"Hello, {args.name}")
    else:
        print(f"Name:{args.name}")
    
    if args.beatiful:
        print(f'{args.name} you are 100% beatiful!')
    else:
        print(f"I can't see you beatiful")
    
    
if __name__ == "__main__":
    main()