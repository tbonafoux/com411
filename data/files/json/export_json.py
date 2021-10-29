import json

def read(path):
    print("Reading...")
    with open(path) as file:
        data = json.load(file)
        print("Done!")
        return data


def save(save_path, data):
    print("Exporting...")
    with open(save_path, "w") as save_file:
        json.dump(data, save_file, indent=4)
        print("Done!")



def run():
    json_data = read("robocity.json")
    save("exported.json", json_data)

if __name__ == "__main__":
  run()