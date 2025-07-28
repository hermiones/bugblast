import argparse
from fuzzers.sql_injection import run_sql_fuzz

def main():
    parser = argparse.ArgumentParser(description="BugBlast API Fuzzer")
    parser.add_argument("-i", "--input", help="File with API endpoints", required=True)
    args = parser.parse_args()

    with open(args.input, 'r') as file:
        endpoints = [line.strip() for line in file]

    for endpoint in endpoints:
        print(f"[+] Fuzzing {endpoint}")
        run_sql_fuzz(endpoint)

if __name__ == "__main__":
    main()
