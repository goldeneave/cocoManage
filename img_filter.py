"""

In filter.py, it filtered the certain category from the dataset, but it did not filtered the corresponding the imgs, so the script will move the img into new folder
FOR COCO FORMAT!

"""
import json
import shutil

# open and load the json file
with open('19677train_ann.json', 'r') as f:
    data = json.load(f)

# print the number of img files in coco format annotation first
file_names = [img['file_name'] for img in data['images']]
num_file_names = len(set(file_names))

print('Number of file names: ', num_file_names)

# define the source and destination folders
# reserve the slash
src_folder = 'D:/all_about_python/person_set/imgs/train/'
dst_folder = 'D:/all_about_python/person_set/imgs/train_cor/'

# iterate over the file names and copy them from the source to the destination folder
for file_name in file_names:
    src_path = src_folder + file_name
    dst_path = dst_folder + file_name
    shutil.copyfile(src_path, dst_path)


