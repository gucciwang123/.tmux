import os
import psutil
import time

def cpu_percentage():
    print(" %3.1f%%" % psutil.cpu_percent(1))

def cpu_temp():
    tempFile = open("/sys/class/thermal/thermal_zone0/temp")
    cpu_temp = tempFile.read()
    tempFile.close()

    print(" %2.1f °C" % (float(cpu_temp)/1000))

def memory_usage():
    print("  %3.2f GiB" % (float(psutil.virtual_memory().used)/1073741824))

def get_upload():
    interface = 'eno1'

    netio = psutil.net_io_counters(pernic=True)

    init_bytes = float(netio[interface].bytes_sent)/1024
    time.sleep(0.25)

    netio = psutil.net_io_counters(pernic=True)
    final_bytes = float(netio[interface].bytes_sent)/1024

    print("  %.2f KiB/s" % ((final_bytes - init_bytes)/.25))

def get_download():
    interface = 'eno1'

    netio = psutil.net_io_counters(pernic=True)

    init_bytes = float(netio[interface].bytes_recv)/1024
    time.sleep(0.25)

    netio = psutil.net_io_counters(pernic=True)
    final_bytes = float(netio[interface].bytes_recv)/1024

    print("  %.2f KiB/s" % ((final_bytes - init_bytes)/0.25))
