from PIL import Image
# from IPython.display import display
import random
import json
import os


# Nombre de objetos y sus probabilidades
cuerpo = ["Verde", "Gris"]
cuerpo_weights = [50, 50]

panzas = ["Verde", "Gris", "Capitan america"]
panzas_weights = [80, 18, 2]

ojos = ["Red regular", "Black Regular", "Ojos loco",
        "orange", "Ojos salido", "Ojos recto"]
ojos_weights = [30, 30, 2, 6, 2, 30]

brazos = ["Verde", "Gris"]
brazos_weights = [90, 10]

acc_brazos = ["Banana", "Guantes", "Unas", "Pulsera UA"]
acc_brazos_wheights = [80, 5, 10, 5]


# Ruta a las las imagenes
cuerpo_files = {
    "Verde": "cuerpo1",
    "Gris": "cuerpo2"
}

panzas_files = {
    "Verde": "panza1",
    "Gris": "panza2",
    "Capitan america": "panza3"
}


brazos_files = {
    "Verde": "brazo1",
    "Gris": "brazo2"
}

acc_brazos_files = {
    "Banana": "acc1",
    "Guantes": "acc2",
    "Unas": "acc3",
    "Pulsera UA": "acc4"
}


ojos_files = {
    "Red regular": "ojos1",
    "Black Regular": "ojos2",
    "Ojos loco": "ojos3",
    "orange": "ojos4",
    "Ojos salido": "ojos5",
    "Ojos recto": "ojos6"
}

TOTAL_IMAGES = 100  # Total de imagenes que queremos generar

all_images = []

# Funcion recursiva para generar una imagen con combinacion unica


def create_new_image():

    new_image = {}

    # For each trait category, select a random trait based on the weightings
    new_image["Cuerpo"] = random.choices(cuerpo, cuerpo_weights)[0]
    new_image["Panza"] = random.choices(panzas, panzas_weights)[0]
    new_image["Brazos"] = random.choices(brazos, brazos_weights)[0]
    new_image["Acc Brazos"] = random.choices(
        acc_brazos, acc_brazos_wheights)[0]
    new_image["Ojos"] = random.choices(ojos, ojos_weights)[0]

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


##############################################################################################

#####                          Generamos las imagenes                               ##########

##############################################################################################


for item in all_images:

    im1 = Image.open(
        f'./images/cuerpo/{cuerpo_files[item["Cuerpo"]]}.png').convert('RGBA')
    im2 = Image.open(
        f'./images/panza/{panzas_files[item["Panza"]]}.png').convert('RGBA')
    im3 = Image.open(
        f'./images/brazo/{brazos_files[item["Brazos"]]}.png').convert('RGBA')
    im4 = Image.open(
        f'./images/accesorios_brazo/{acc_brazos_files[item["Acc Brazos"]]}.png').convert('RGBA')
    im5 = Image.open(
        f'./images/ojos/{ojos_files[item["Ojos"]]}.png').convert('RGBA')

    # Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)

    # Convert to RGB
    rgb_im = com4.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/result/" + file_name)
