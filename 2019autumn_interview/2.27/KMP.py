def KMP(main_str, model_str):
    i, j = 0, 0
    next_list = next_KMP_init(model_str)
    while i < len(main_str) and j < len(model_str):
        if j == -1 or main_str[i] == model_str[j]:
            i += 1
            j += 1
        else:
            j = next_list[j]

    if j == len(model_str):
        return i - j
    else:
        return -1


def next_KMP(model_str):
    next_list = list(range(len(model_str)))

    for i in range(len(model_str)):
        j = i
        while model_str[:j] != model_str[i + 1 - j:i + 1] and j > 0:
            j -= 1
        next_list[i] = j

    ret_list = next_list[:-1]
    ret_list.insert(0, -1)
    return ret_list


def next_KMP_init(model_str):
    next_list = list(range(len(model_str)))
    print(next_list)
    next_list[0] = -1
    i, j = 0, -1
    while i < len(model_str) - 1:
        if j == -1 or model_str[i] == model_str[j]:
            i += 1
            j += 1
            next_list[i] = j
        else:
            j = next_list[j]
    print(next_list)
    return next_list

model_str = 'abababca'
next_list = next_KMP_init(model_str)
