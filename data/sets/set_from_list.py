def observed():
    observations = []
    for x in range(7):
        obs = input("What do they see?\n")
        observations.append(obs)
    return observations


def run():
    print("Counting observations")
    observations = observed()
    obs_set = set(observations)
    obs_counted_list = []
    obs_counted_set = set()
    for item in obs_set:
        item_count = observations.count(item)
        obs_counted_list.append((item, item_count))
    obs_counted_set =  set(obs_counted_list)
    print(obs_counted_set)

run()