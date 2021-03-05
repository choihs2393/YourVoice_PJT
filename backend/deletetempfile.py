import os
import glob

[os.remove(f) for f in glob.glob("./data/mp42/*.temp")]
os.remove("./data/mp42/collectMP3.py")