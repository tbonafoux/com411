def observed():
    observation = []
    for x in range(5):
        observation.append(input("Enter an observation.\n"))
    return observation

def remove_observations(list):
    obs = list
    loop = True
    while loop:
        user_input = input("Do you wish to remove an ob? (y/n)\n")
        if user_input.lower() == "y":
            ob_to_remove = input("What ob do you want to remove?")
            obs.remove(ob_to_remove)
        else:
            loop = False
    return obs

def run():
    list =observed()
    updated_list = remove_observations(list)
    counted_list = []
    for ob in set(updated_list):
        item_count = updated_list.count(ob)
        counted_list.append((ob, item_count))
    print(counted_list)


if __name__ == "__main__":
    run()
