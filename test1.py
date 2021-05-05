import psutil
import pandas as pd
import openpyxl

def this_is():
	test = psutil.disk_io_counters(perdisk=True)
	converted = list(test.values())
	return converted






