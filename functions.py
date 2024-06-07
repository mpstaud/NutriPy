def maintenance_calories(current_weight):
    result = current_weight * 15
    return result


def lose_one_lb_per_week(current_weight):
    result = maintenance_calories(current_weight) - 500
    return result


def lose_two_lbs_per_week(current_weight):
    result = maintenance_calories(current_weight) - 1000
    return result


def gain_one_lb_per_week(current_weight):
    result = maintenance_calories(current_weight) + 500
    return result


def gain_two_lbs_per_week(current_weight):
    result = maintenance_calories(current_weight) + 1000
    return result