import numpy as np
import pickle
src = '../trdg/font_utils/colors_new.cp'
dst = src + ".tmp"
data = open(src, 'rb').read()
data=data.replace(b"\r\n", b"\n")
print(data)
with open('result.pickle', 'wb') as f: # b for binary
    pickle.dump(data, f)


# print(np.fromfile(src).shape)
# with open("result.pickle", "rb") as f:
#     u = pickle._Unpickler(f)
#     u.encoding = 'latin1'
#     p = u.load()
#     print(p.shape)
#
#
# with open('result.pickle', 'rb') as f: # b for binary
#     obj = pickle.load(f)
# print(obj.shape)
# # pickle.load(open(src,'rb'), encoding='latin-1')