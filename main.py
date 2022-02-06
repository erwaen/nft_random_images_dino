from PIL import Image
# from IPython.display import display
import random
import json
import os
import math
import data as my_data
import tools as my_tools


# # Nombre de objetos y sus probabilidades
# cuerpo = ["Verde", "Gris"]
# cuerpo_weights = [50, 50]

# panzas = ["Verde", "Gris", "Capitan america"]
# panzas_weights = [80, 18, 2]

# ojos = ["Red regular", "Black Regular", "Ojos loco",
#         "orange", "Ojos salido", "Ojos recto"]
# ojos_weights = [30, 30, 2, 6, 2, 30]

# brazos = ["Verde", "Gris"]
# brazos_weights = [90, 10]

# acc_brazos = ["Banana", "Guantes", "Unas", "Pulsera UA"]
# acc_brazos_wheights = [80, 5, 10, 5]


# Ruta a las las imagenes
# cuerpo_files = {
#     "Verde": "cuerpo1",
#     "Gris": "cuerpo2"
# }

# panzas_files = {
#     "Verde": "panza1",
#     "Gris": "panza2",
#     "Capitan america": "panza3"
# }


# brazos_files = {
#     "Verde": "brazo1",
#     "Gris": "brazo2"
# }

# acc_brazos_files = {
#     "Banana": "acc1",
#     "Guantes": "acc2",
#     "Unas": "acc3",
#     "Pulsera UA": "acc4"
# }


# ojos_files = {
#     "Red regular": "ojos1",
#     "Black Regular": "ojos2",
#     "Ojos loco": "ojos3",
#     "orange": "ojos4",
#     "Ojos salido": "ojos5",
#     "Ojos recto": "ojos6"
# }

TOTAL_IMAGES = int(input("How many images do you want to generate?: "))  # Total de imagenes que queremos generar

all_images = []

# Funcion recursiva para generar una imagen con combinacion unica


def create_new_image():

    new_image = {}

    # For each trait category, select a random trait based on the weightings
    new_image["background_color"] = random.choices(
        my_data.background_color, my_data.background_color_weights)[0]

    new_image["environment"] = random.choices(
        my_data.environment, my_data.environment_weights)[0]

    new_image["body"] = random.choices(my_data.body, my_data.body_weights)[0]

    new_image["belly"] = random.choices(
        my_data.belly, my_data.belly_weights)[0]

    new_image["back"] = random.choices(my_data.back, my_data.back_weights)[0]

    new_image["legs"] = random.choices(my_data.legs, my_data.legs_weights)[0]

    new_image["arms"] = random.choices(my_data.arms, my_data.arms_weights)[0]

    new_image["necklace"] = random.choices(
        my_data.necklace, my_data.necklace_weights)[0]

    new_image["mouth"] = random.choices(
        my_data.mouth, my_data.mouth_weights)[0]

    new_image["acc_arms"] = random.choices(
        my_data.acc_arms, my_data.acc_arms_weights)[0]

    new_image["eyes"] = random.choices(my_data.eyes, my_data.eyes_weights)[0]

    new_image["hat"] = random.choices(my_data.hat, my_data.hat_weights)[0]

    if new_image in all_images:
        return create_new_image()
    else:
        return new_image


# Genera combinaciones unica dependiendo de los rasgos
for i in range(TOTAL_IMAGES):

    new_trait_image = create_new_image()

    all_images.append(new_trait_image)


# VERIFICAMOS QUE TODAS LAS IMAGENES SEAN UNICAS YA QUE ES IMPORTANTE

# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)


print("Are all images unique?", all_images_unique(all_images))
# Add token Id to each image
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1

print(all_images)


##############################################################################################

#####       ACA PODEMOS PONER CODIGO PARA SABER CUANTAS VECES SE REPITIO CADA RASGO ##########

##############################################################################################

traits_counts = {}
for trait in my_data.traits_names:
    traits_counts[trait] = {}

print( traits_counts)

for item in my_data.background_color:
    traits_counts["background_color"][item] = 0

for item in my_data.environment:
    traits_counts["environment"][item] = 0

for item in my_data.body:
    traits_counts["body"][item] = 0

for item in my_data.belly:
    traits_counts["belly"][item] = 0

for item in my_data.back:
    traits_counts["back"][item] = 0

for item in my_data.legs:
    traits_counts["legs"][item] = 0

for item in my_data.arms:
    traits_counts["arms"][item] = 0

for item in my_data.necklace:
    traits_counts["necklace"][item] = 0

for item in my_data.mouth:
    traits_counts["mouth"][item] = 0

for item in my_data.acc_arms:
    traits_counts["acc_arms"][item] = 0

for item in my_data.hat:
    traits_counts["hat"][item] = 0

for item in my_data.eyes:
    traits_counts["eyes"][item] = 0

for image in all_images:
    traits_counts["background_color"][image["background_color"]] +=1
    traits_counts["environment"][image["environment"]] +=1
    traits_counts["body"][image["body"]] +=1
    traits_counts["belly"][image["belly"]] +=1
    traits_counts["back"][image["back"]] +=1
    traits_counts["legs"][image["legs"]] +=1
    traits_counts["arms"][image["arms"]] +=1
    traits_counts["necklace"][image["necklace"]] +=1
    traits_counts["mouth"][image["mouth"]] +=1
    traits_counts["acc_arms"][image["acc_arms"]] +=1
    traits_counts["hat"][image["hat"]] +=1
    traits_counts["eyes"][image["eyes"]] +=1

print("\n\n\n==================\n==================\n")

for trait_key, trait_value in traits_counts.items():
    print(f'{trait_key}:')
    for item_key, item_value in trait_value.items():
        print(f'\t{item_key}: {item_value}')
    print()


print("\n\n\n==================\n==================\n")

my_tools.write_traits_counts_in_a_txt_and_json(traits_counts)




##############################################################################################

#####                          Generamos las imagenes                               ##########

##############################################################################################


for item in all_images:

    im1 = Image.open(
        f'./images/background_color/{my_data.background_color_files[item["background_color"]]}.png').convert('RGBA')

    im2 = Image.open(
        f'./images/environment/{my_data.environment_files[item["environment"]]}.png').convert('RGBA')

    im3 = Image.open(
        f'./images/body/{my_data.body_files[item["body"]]}.png').convert('RGBA')

    im4 = Image.open(
        f'./images/belly/{my_data.belly_files[item["belly"]]}.png').convert('RGBA')

    # im5 = Image.open(
    #     f'./images/tail/{my_data.tail_files[item["tail"]]}.png').convert('RGBA')

    im5 = Image.open(
        f'./images/back/{my_data.back_files[item["back"]]}.png').convert('RGBA')

    im6 = Image.open(
        f'./images/legs/{my_data.legs_files[item["legs"]]}.png').convert('RGBA')

    im7 = Image.open(
        f'./images/arms/{my_data.arms_files[item["arms"]]}.png').convert('RGBA')

    im8 = Image.open(
        f'./images/necklace/{my_data.necklace_files[item["necklace"]]}.png').convert('RGBA')

    im9 = Image.open(
        f'./images/mouth/{my_data.mouth_files[item["mouth"]]}.png').convert('RGBA')

    im10 = Image.open(
        f'./images/acc_arms/{my_data.acc_arms_files[item["acc_arms"]]}.png').convert('RGBA')

    im11 = Image.open(
        f'./images/eyes/{my_data.eyes_files[item["eyes"]]}.png').convert('RGBA')

    im12 = Image.open(
        f'./images/hat/{my_data.hat_files[item["hat"]]}.png').convert('RGBA')

    # # Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)
    com5 = Image.alpha_composite(com4, im6)
    com6 = Image.alpha_composite(com5, im7)
    com7 = Image.alpha_composite(com6, im8)
    com8 = Image.alpha_composite(com7, im9)
    com9 = Image.alpha_composite(com8, im10)
    com10 = Image.alpha_composite(com9, im11)
    com11 = Image.alpha_composite(com10, im12)

    # Convert to RGB
    rgb_im = com11.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/result/" + file_name)
