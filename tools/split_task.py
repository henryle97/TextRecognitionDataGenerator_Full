import glob
import random
import numpy as np
import os
import shutil

sub_dir = ["hoang", 'nam', 'vy', 'lien']
done_dir = "splitted"
if not os.path.exists(done_dir):
    os.mkdir(done_dir)
paths = glob.glob("*/*.jpg")
total_img = len(paths)

done_array = np.array_split(paths, len(sub_dir))

for i, name in enumerate(sub_dir):
    arr = done_array[i]

    if not os.path.exists(done_dir + "/" + name):
        os.mkdir(done_dir + "/" + name)
    for path in arr:
        src = path
        dest = done_dir + "/" +sub_dir[i] + "/"+ os.path.basename(src)
        shutil.copy(src, dest)

        src = path.split(".")[0] + ".txt"
        dest = done_dir + "/" + sub_dir[i] + "/"+ os.path.basename(src)
        shutil.copy(src, dest)
