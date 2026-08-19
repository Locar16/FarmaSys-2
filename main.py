import sys

def main():
    if len(sys.argv) > 1:
        for item in sys.argv[1:]:
            print("Olá, ", item + "!")
    else:
        print("Olá mundo!")
if __name__ == "__main__":
    main()