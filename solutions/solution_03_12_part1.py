import re

with open("data/input_03_12.txt", "r") as f:
    input = f.readlines()


def get_value(text):
    total_sum = 0
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
            current_row = row[look_idx_s] + row[look_idx_e]
            next_row = matrix_text[min(idx + 1, len(matrix_text) - 1)][
                look_idx_s : look_idx_e + 1
            ]

            # replace all digits by .
            candidates = re.sub(r"\d", ".", pre_row + current_row + next_row)
            # get all characters we have in the surrounding and remove '.'
            candidates = set(candidates)
            candidates.remove(".")
            # if there are symbols, add the number
            if len(candidates) > 0:
                total_sum += int(c)

    return total_sum


print("Solution: ", end="")
print(get_value(input))
