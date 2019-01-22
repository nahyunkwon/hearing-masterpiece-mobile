import json
import time
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
import numpy as np
import copy
import itertools

import os
from collections import defaultdict
import sys
from pprint import pprint

from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pprint

dataset = json.load(open("./plot_image_segmentation_web/instances_val2017.json", 'r'))

print("hil")

