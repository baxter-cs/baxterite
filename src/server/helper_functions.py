import config


def convert_grade(grade):
    if grade in config.baxter_five:
        return config.baxter_five[grade]
    elif grade in config.old_grading:
        return config.old_grading[grade]
    else:
        return 0
