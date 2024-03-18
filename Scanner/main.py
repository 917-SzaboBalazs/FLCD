from scanner import Scanner

def main():
    scanner = Scanner("p1.py")
    scanner.scan()
    scanner.log_to_file()

if __name__ == "__main__":
    main()