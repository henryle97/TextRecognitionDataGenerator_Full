import os

root_dir = 'id'
paths = os.listdir(root_dir)
test_size = 0.1
test_size_idx = int(len(paths) * test_size)

train_paths = paths[test_size_idx:]
test_paths = paths[:test_size_idx]


with open("train_id.txt", 'w') as f:
    for path in train_paths:
        label = path.split("_")[1]
        path_img = root_dir + "/" + path + "\t" + label
        f.write(path_img + "\t")

with open("test_id.txt", 'w') as f:
    for path in test_paths:
        label = path.split("_")[1]
        path_img = root_dir + "/" + path + "\t" + label
        f.write(path_img + "\t")





