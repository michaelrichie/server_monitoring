import psutil
from datetime import date,time
import openpyxl
from test1 import this_is

def main():
	tanggal = date.today()
	b = str(float(get_cpu_usage_pct()))
	c = str(float(get_ram_usage() / 1024 / 1024/1024))
	d = str(float(get_ram_total() / 1024 / 1024/1024))
	e = str(get_ram_usage_pct())
	f = str(get_disk_usage())
	with open('test.txt','a') as files :
		files.write(str(f"{tanggal}\n"))
		files.write(f"CPU usage : {b}\n")
		files.write(f"RAM Usage : {c} GB > {e}%\n")
		files.write(f"RAM Total : {d} GB \n")
		files.write(f"{f}\n\n\n\n\n")	


def get_cpu_usage_pct():
    return psutil.cpu_percent(interval=0.5)
def get_ram_usage():
    return int(psutil.virtual_memory().total - psutil.virtual_memory().available)
def get_ram_total():
    return int(psutil.virtual_memory().total)
def get_ram_usage_pct():
    return psutil.virtual_memory().percent
def get_disk_usage():
    return this_is()

if __name__ == "__main__" : 
	main()

