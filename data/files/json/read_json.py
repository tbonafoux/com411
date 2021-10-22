import json

def read(path):
    with open("robocity.json") as file:
        data = json.load(file)
        print(f"City Name: {data['city']}")
        print(f"Population Size: {data['population']}")
        for bot in data["bots"]:
            print(f"{bot['name']} has a strength level of {bot['stats']['strength'] }"
                  f"and a speed of {bot['stats']['speed']}.")


def run():
    read("robocity.json")

if __name__ == "__main__":
  run()