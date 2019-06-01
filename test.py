import glob
import os
PATH = "."

g = [os.path.basename(i) for i in glob.glob("{}\\*".format(PATH))]
print(g)