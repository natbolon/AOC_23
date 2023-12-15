import re

with open("data/input_03_12.txt", "r") as f:
    input = f.readlines()


def get_potential_gears(text):
    case = {}
    if isinstance(text, str):
        matrix_text = text.split("\n")
    else:
        matrix_text = text
    for idx, row in enumerate(matrix_text):
        # print('New row: ', idx)
        row = row.strip()
        for match in re.finditer(r"\d+", row):
            c = match.group()
            s = match.start()
            e = match.end() - 1

            look_idx_s = max(s - 1, 0)
            look_idx_e = min(len(row) - 1, e + 1)

            # select surrounding cells
            pre_row = matrix_text[max(idx - 1, 0)][look_idx_s : look_idx_e + 1]
            next_row = matrix_text[min(idx + 1, len(matrix_text) - 1)][
                look_idx_s : look_idx_e + 1
            ]

            r, col = None, None
            if "*" in pre_row:
                r = max(idx - 1, 0)
                col = look_idx_s + pre_row.index("*")

            elif "*" == row[look_idx_s]:
                r = idx
                col = look_idx_s

            elif "*" == row[look_idx_e]:
                r = idx
                col = look_idx_e

            elif "*" in next_row:
                r = min(idx + 1, len(matrix_text) - 1)
                col = look_idx_s + next_row.index("*")

            v = case.get((r, col), [])
            v.append(int(c))
            case[(r, col)] = v

    return case


def get_sum_gear(case):
    total_gear_sum = 0
    for k, v in case.items():
        if len(v) == 2 and k[0] is not None:
            total_gear_sum += v[0] * v[1]
    return total_gear_sum


case = get_potential_gears(input)
print("Solution: ", get_sum_gear(case))
