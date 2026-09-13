from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    max_res = []
    for ls in nested_arr:
        max_el = ls[0] if ls[0] else None
        for el in ls:
            max_el = max(max_el, el)
        max_res.append(max_el)
    return max_res


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
