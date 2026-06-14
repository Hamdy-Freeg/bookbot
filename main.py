import sys
from report import format

def main() :
    filepath = sys.argv[1]
    format(filepath)
    
main()