import json 

def write_traits_counts_in_a_txt_and_json(traits_counts):
    with open("./images/result/traits_count.json", "w") as f:
        json.dump(traits_counts, f, indent=4, sort_keys=True)
    with open("./images/result/traits_count.txt", "w") as f:
        for trait_key, trait_value in traits_counts.items():
            f.write(f'{trait_key}:\n')
            for item_key, item_value in trait_value.items():
                f.write(f'\t{item_key}: {item_value}\n')
            f.write("\n")
