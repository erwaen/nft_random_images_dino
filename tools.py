import json 
import os

from importlib_metadata import metadata

def write_traits_counts_in_a_txt_and_json(traits_counts):
    with open("./images/result/traits_count.json", "w") as f:
        json.dump(traits_counts, f, indent=4, sort_keys=True)

    with open("./images/result/traits_count.txt", "w") as f:
        for trait_key, trait_value in traits_counts.items():
            f.write(f'{trait_key}:\n')
            for item_key, item_value in trait_value.items():
                f.write(f'\t{item_key}: {item_value}\n')
            f.write("\n")


def create_metadata_all_traits(all_images):
    #### Generate Metadata for all Traits 
    if not os.path.exists("./metadata"):
        os.mkdir(f'./metadata')

    METADATA_FILE_NAME = './metadata/all-traits.json'; 
    with open(METADATA_FILE_NAME, 'w') as outfile:
        json.dump(all_images, outfile, indent=4)



def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }

def generate_metadata_for_each_image():
    
    with open("./metadata/all-traits.json", "r") as f:
        data = json.load(f)

        # Cambiar URL al generar nuevas imagenes
        IMAGES_BASE_URL = "https://https://gateway.pinata.cloud/ipfs/QmWN4jKxP1356Nn2Q4FwjNMTjgjxhBbS4J9tkj1XeM5pvy/"
        PROJECT_NAME = "NFT_DINO"

        for i in data:
            token_id = i["tokenId"]
            token = {
                "image": IMAGES_BASE_URL + str(token_id) + '.png',
                "tokenId": token_id,
                "name": PROJECT_NAME + ' ' + str(token_id),
                "attributes": []
            }
            token["attributes"].append(getAttribute("background_color", i["background_color"]))
            token["attributes"].append(getAttribute("environment", i["environment"]))
            token["attributes"].append(getAttribute("body", i["body"]))
            token["attributes"].append(getAttribute("belly", i["belly"]))
            token["attributes"].append(getAttribute("back", i["back"]))
            token["attributes"].append(getAttribute("legs", i["legs"]))
            token["attributes"].append(getAttribute("arms", i["arms"]))
            token["attributes"].append(getAttribute("necklace", i["necklace"]))
            token["attributes"].append(getAttribute("mouth", i["mouth"]))
            token["attributes"].append(getAttribute("acc_arms", i["acc_arms"]))
            token["attributes"].append(getAttribute("eyes", i["eyes"]))
            token["attributes"].append(getAttribute("hat", i["hat"]))

            with open("./metadata/" + str(token_id) + ".json", "w") as outfile:
                json.dump(token, outfile, indent=4)
            




