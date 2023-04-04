import psutil

cpu = psutil.cpu_freq()
print(cpu)

cpu_core = psutil.cpu_count(logical=False)  # 물리코어
print(cpu_core)
cpu_core = psutil.cpu_count()  # 논리 프로세서
print(cpu_core)

memory = psutil.virtual_memory()
print(memory)

disk = psutil.disk_partitions()
print(disk)

net = psutil.net_io_counters()
print(net)
