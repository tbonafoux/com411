import csv

def extract(path):
    print("Extracting...\n", end = "")
    names = ""
    with open("bots.csv") as file:
        data = csv.reader(file)
        head = next(data)
        for row in data:
            names = names + row[1] + "\n"
    print(f"The extracted names are:\n"
          f"{names}")

def run():
    extract("bots.csv")

if __name__ == "__main__":
  run()
