"""
    File Name: 补充：检查Ghostscript是否可用
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/2 22:16
"""

import ctypes
from ctypes.util import find_library
find_library("".join(("gsdll", str(ctypes.sizeof(ctypes.c_voidp) * 8), ".dll")))
