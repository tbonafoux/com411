def climb_ladder(steps, moved):
    if steps < moved:
        print("Still some way to go!")
    else:
        print("We are almost there!")


climb_ladder(5, 2)
climb_ladder(2, 5)

