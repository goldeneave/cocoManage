# Description for the repo
When I use some dataset, it usually can not satisfy my requirement directly, so I should make some modification on them, in the repo, I will attach some code I used to handle dataset, for backup and also wish could help someone in need

## filter.py
It is collect from [here](https://github.com/immersive-limit/coco-manager), thanks for the job! And if you use the script you should follow the format like: python filter.py --input_json <*origin data annotation path*> output_json <*path you want to save*> --categories <*categories you want extract*>, but it seems could not extract img file either, so I write the following script the move corresponding img from dataset folder to where you set

## img_filter.py

The script is used to copy img files form src folder to dst folder, and I also write the snippet to calculate the number of images exist in annotation files, so just set your path

## seg_check.py

The code script will check whether your coco annotation has correct segmentation infos
For me, FashionPedia dataset, it has a key value called "counts", which do not hava ang seg infos.
So I write the script to check segmentation infos

## set_size.py
When I extract data from coco-stuff, it is too many for me, I should also maintain the balance between different category imgs, so I should only save a certain number.
The first step is to save a correct number of annotation, then move the img file.

## coco_test.py

After extract and set your dataset size, you could test the segmentation, the code will draw polygons in randomly chose img files
