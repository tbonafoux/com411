def export(path, num_bots):
    print("Exporting...")
    for x in range(num_bots):
        bot_id = input("Please enter the bot id:\n")
        bot_name = input("Please enter the bot name:\n")
        bot_paint = input("Please enter the bot paint:\n")
        with open(path, "a") as file:
            file.write(f"{bot_id},{bot_name},{bot_paint}\n")
    print("\nDone!")

def run():
    export("bots.csv", 2)

if __name__ == "__main__":
  run()