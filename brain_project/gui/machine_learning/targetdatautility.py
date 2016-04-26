

def convert_targets_to_simple_values(targets):
    result_targets = []

    for target in targets:

        temp_result = convert_target_to_simple_value(target)

        result_targets.append(temp_result)

    return result_targets

def convert_target_to_simple_value(target):

    if target > 0:
        return 1
    elif target < 0:
        return -1
    else:
        return 0 