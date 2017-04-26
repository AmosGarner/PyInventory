import argparse as args

def generateArgumentsFromParser():
    parser = parser = argparse.ArgumentParser(description="Runs PyInventory personal inventory manager program.")
    parser.add_argument('--name', dest='collection_name', required=True)
    return parser.parse_args()

def main():
    arguments = generateArgumentsFromParser()

if __name__ == '__main__':
    main()
