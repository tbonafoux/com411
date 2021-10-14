def escape_by(plan):
    if plan.lower() == "jumping over":
        print("The boulder is too big!")
    elif plan.lower() == "running around":
        print("The boulder is too fast!")
    elif plan.lower() == "going deeper":
        print("That might just work! Let's go deeper!")


escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")