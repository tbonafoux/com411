import csv

def read(path):
    with open(path) as file:
        data = csv.reader(file)
        head = next(data)
        print(f"Headings:\n"
              f"{head}\n"
              f"Values:")
        for row in data:
            print(row)

def run():
    read("bots.csv")

if __name__ == "__main__":
  run()