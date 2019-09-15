import os

# Need to have to dataset folder
path = '../train-dataset'
files = []
plant_disease_dict = {}
# r=root, d=directories, f = files
# for r, d, f in os.walk(path):
#     folders_name = r.split("/")
#     if len(folders_name) == 2:
#         continue
#     plant_disease = folders_name[2].split("__")
#     if len(plant_disease) <= 1:
#         continue
#     plant, disease_underscore = plant_disease
#     disease = disease_underscore.replace("_", " ")
#     disease = disease[1: len(disease)]
#     if plant in plant_disease_dict:
#         plant_disease_dict[plant].append(disease)
#     else:
#         plant_disease_dict[plant] = [disease]
# print(plant_disease_dict)

for r, d, f in os.walk(path):
    files = f
print(len(files))