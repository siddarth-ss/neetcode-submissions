from typing import Dict, List, Tuple


def get_dict_items(age_dict: Dict[str, int]) -> List[Tuple[str, int]]:
    keys= list(age_dict.keys())
    values = list(age_dict.values())

    output= [(x,y)for x,y in zip(keys,values)]
    return output

        




# do not modify below this line
print(get_dict_items({'Alice': 25, 'Bob': 30, 'Charlie': 35}))
print(get_dict_items({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}))
print(get_dict_items({'Bob': 30, 'David': 40, 'Charlie': 35, 'Alice': 25, 'Eve': 45}))
print(get_dict_items({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40, 'Eve': 45, 'Frank': 50}))
