import os
import sys

assert sys.version_info.major >= 3, 'Error: please use python3.'

assert os.environ.get('DISPLAY', None), (
    "Error: DISPLAY is not set. \n" +
    "Run 'export DISPLAY=:0.0' if you're SSHing to Raspberry Pi")
