# Nombre de objetos y sus probabilidades

def name_to_file_path(list_of_names):
    dictionary_to_return = {}
    for name in list_of_names:
        dictionary_to_return[name] = name

    return dictionary_to_return


background_color = ["normal_1", "normal_2", "normal_3", "normal_4", "normal_5", "normal_6",
                    "epic_dark_blue"]
background_color_weights = [10, 20, 10, 10, 20, 20, 10]


environment = ["sun_clouds_drones", "sun_planes_helicopters", "meteorites", "japanese_poster",
               "burning_city", "beach", "eggs", "night_city", "trees_and_houses", "dino_park"]
environment_weights = [10, 10, 10, 10, 10, 10,
                       10, 10, 10, 10]


body = ["gray", "green", "dark_gray"]
body_weights = [40, 40, 20]


belly = ["gray", "green", "cream", "purple", "yellow", "red", "child",
         "yin_yang_symbol", "super_belly", "american_belly", "lantern_belly"]
belly_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 5, 5]


back = ["green", "brown", "pink", "light_blue",
        "blue", "thunder", "epic_blue", "epic_purple"]
back_weights = [20, 20, 10, 10, 10, 10, 10, 10]


legs = ["gray", "green", "dark_gray", "builder",
        "earth", "ball", "wheels", "wheelchair", "fried_chicken"]
legs_weights = [20, 10, 10, 10, 10, 10, 10, 10, 10]


arms = ["Gray", "Green",  "dark_gray", "Skull_gray", "Skull_green", "Rainbow_gray",
        "Rainbow_green", "Moab_gray", "Moab_green", "Nuke_gray", "Nuke_green", "God_green"]
arms_weights = [10, 10, 20, 20, 10, 10, 10, 2, 2, 2, 2, 2]


necklace = ["spike", "whistle", "red_scarf",
            "green_scarf", "purple_scarf", "christmas_scarf"]
necklace_weights = [30, 20, 20, 10, 10, 10]


mouth = ["normal_teeth", "gold_tooth", "fire",
         "laser_beam", "bubbles", "tongue_teeth_saliva"]
mouth_weights = [30, 20, 20, 10, 10, 10]


acc_arms = ["Banana", "Glove_with_gems", "Smartphone", "Boxing_gloves",
            "Watch_brown_band", "Watch_white_band", "Bracelet_G", "p_ball", "Chains", "Bracelet_UA", "snack"]
acc_arms_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 5, 5]


eyes = ["regular_black", "regular_green", "regular_blue", "red", "straight", "in_love",
        "tears", "cross_eyed", "tired", "eyes_out"]
eyes_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

hat = ["black", "mexican", "teletubie", "santa_claus",
       "chef", "pirate", "crown", "black_hair", "rainbow_hair"]
hat_weights = [20, 10, 10, 10, 10, 10, 10, 10, 10]


print("background_color: ", len(background_color))
print("environment: ", len(environment))
print("body: ", len(body))
print("belly: ", len(belly))

print("back: ", len(back))
print("legs: ", len(legs))
print("arms: ", len(arms))
print("necklace: ", len(necklace))
print("mouth: ", len(mouth))
print("acc_arms: ", len(acc_arms))
print("eyes: ", len(eyes))
print("hat: ", len(hat))


# Ruta a las las imagenes


background_color_files = {}
background_color_files = name_to_file_path(background_color)

environment_files = {}
environment_files = name_to_file_path(environment)

body_files = {}
body_files = name_to_file_path(body)

belly_files = {}
belly_files = name_to_file_path(belly)


back_files = {}
back_files = name_to_file_path(back)

legs_files = {}
legs_files = name_to_file_path(legs)

arms_files = {}
arms_files = name_to_file_path(arms)

necklace_files = {}
necklace_files = name_to_file_path(necklace)

mouth_files = {}
mouth_files = name_to_file_path(mouth)

acc_arms_files = {}
acc_arms_files = name_to_file_path(acc_arms)

eyes_files = {}
eyes_files = name_to_file_path(eyes)

hat_files = {}
hat_files = name_to_file_path(hat)

# background_color_files = {
#     "normal_1": "normal_1",
#     "normal_2": "normal_2",
#     "normal_3": "normal_3",
#     "normal_4": "normal_4",
#     "normal_5": "normal_5",
#     "normal_6": "normal_6",
#     "normal_7": "normal_7",
#     "normal_8": "normal_8",
#     "normal_9": "normal_9",
#     "normal_10": "normal_10",
#     "normal_11": "normal_11",
#     "normal_12": "normal_12",
#     "normal_13": "normal_13",
#     "normal_14": "normal_14",
#     "normal_blue": "normal_blue",
#     "epic_dark_blue": "epic_dark_blue",
# }

# environment_files = {
#     "sun_clouds_drones": "sun_clouds_drones",
#     "sun_planes_helicopters": "sun_planes_helicopters",
#     "meteorites": "meteorites",
#     "japanese_poster": "japanese_poster",
#     "burning_city": "burning_city",
#     "beach": "beach",
#     "eggs": "eggs",
#     "night_city": "night_city",
#     "trees_and_houses": "trees_and_houses",
#     "dino_park": "dino_park"
# }

# body_files = {
#     "gray": "gray",
#     "green": "green",
#     "santa_claus": "santa_claus"
# }

# belly_files = {
#     "gray": "gray",
#     "green": "green",
#     "cream": "cream",
#     "child": "child",
#     "purple_green": "purple_green",
#     "yin_yang_symbol": "yin_yang_symbol",
#     "super_belly": "super_belly",
#     "american_belly": "american_belly",
#     "lantern_belly": "lantern_belly",
# }

# tail_files = {
#     "ballet": "ballet"
# }


# back_files = {
#     "green": "green",
#     "brown": "brown",
#     "pink": "pink",
#     "light_blue": "light_blue",
#     "blue": "blue",
#     "thunder": "thunder",
#     "epic_blue": "epic_blue",
#     "epic_purple": "epic_purple"
# }

# legs_files = {
#     "gray": "gray",
#     "green": "green",
#     "chicken": "chicken",
#     "builder": "builder",
#     "boots": "boots",
#     "wheels": "wheels",
#     "wheelchair": "wheelchair",
#     "fried_chicken": "fried_chicken"
# }

# arms_files = {
#     "Gray": "Gray",
#     "Green": "Green",
#     "Red": "Red",
#     "Yellow": "Yellow",
#     "Pink": "Pink",
#     "Skull_gray": "Skull_gray",
#     "Skull_green": "Skull_green",
#     "Rainbow_gray": "Rainbow_gray",
#     "Rainbow_green": "Rainbow_green",
#     "Moab_gray": "Moab_gray",
#     "Moab_green": "Moab_green",
#     "Nuke_gray": "Nuke_gray",
#     "Nuke_green": "Nuke_green",
#     "God_green": "God_green"
# }

# necklace_files = {
#     "spike": "spike",
#     "whistle": "whistle",
#     "red_scarf": "red_scarf",
#     "green_scarf": "green_scarf",
#     "purple_scarf": "purple_scarf",
#     "christmas_scarf": "christmas_scarf"
# }

# mouth_files = {
#     "normal_teeth": "normal_teeth",
#     "gold_tooth": "gold_tooth",
#     "fire": "fire",
#     "laser_beam": "laser_beam",
#     "bubbles": "bubbles",
#     "tongue_teeth_saliva": "tongue_teeth_saliva"
# }

# acc_arms_files = {
#     "Banana": "Banana",
#     "Glove_with_gems": "Glove_with_gems",
#     "Smartphone": "Smartphone",
#     "Boxing_gloves": "Boxing_gloves",
#     "Watch_brown_band": "Watch_brown_band",
#     "Watch_white_band": "Watch_white_band",
#     "Bracelet_G": "Bracelet_G",
#     "Knife": "Knife",
#     "Chains": "Chains",
#     "Bracelet_UA": "Bracelet_UA",
#     "snack": "snack"
# }

# eyes_files = {
#     "red": "red",
#     "straight": "straight",
#     "in_love": "in_love",
#     "tears": "tears",
#     "cross_eyed": "cross_eyed",
#     "tired": "tired",
#     "eyes_out": "eyes_out"
# }

# hat_files = {
#     "black": "black",
#     "mexican": "mexican",
#     "teletubie": "teletubie",
#     "santa_claus": "santa_claus",
#     "chef": "chef",
#     "pirate": "pirate",
#     "crown": "crown",
#     "black_hair": "black_hair",
#     "rainbow_hair": "rainbow_hair",
# }
