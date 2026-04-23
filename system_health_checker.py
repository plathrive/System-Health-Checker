import psutil

# Sekarang mulai tulis function RAM checker-nya. Yang harus function itu tampilkan:
# Total RAM
# RAM yang terpakai
# Persentase pemakaian

def check_ram():
    mem = psutil.virtual_memory()
    bytes_to_gb = pow(1024, 3)
    total_ram = mem.total / bytes_to_gb
    used_ram = mem.used / bytes_to_gb
    percent_ram = mem.percent

    checking = f"Total RAM: {total_ram:.3f} GB\nUsed RAM: {used_ram:.3f} GB\nUsage Percentage: {percent_ram:.2f}%"
    return checking
