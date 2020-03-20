import sys
import os
sys.path.append(os.path.abspath("/test"))
from test import *

test_all();
print("Test cases passed");