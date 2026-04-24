import psutil

# Sekarang mulai tulis function RAM checker-nya. Yang harus function itu tampilkan:
# Total RAM
# RAM yang terpakai
# Persentase pemakaian

def check_ram():
    try:
        mem = psutil.virtual_memory()
        bytes_to_gb = pow(1024, 3)
        total_ram = mem.total / bytes_to_gb
        used_ram = mem.used / bytes_to_gb
        percent_ram = mem.percent

        checking = f"Total RAM: {total_ram:.2f} GB\nUsed RAM: {used_ram:.2f} GB\nUsage Percentage: {percent_ram:.2f}%"
        return checking

    except Exception:
        print(f"Error: Sistem gagal mengakses data process.")
    

# Function apa yang dipakai untuk ngecek penggunaan disk? 
# Dan kira-kira attribute apa yang lu butuhkan berdasarkan requirement tadi: 
# persentase pemakaian, dan warning kalau di atas 80%.

def check_disk():
    try: 
        disk = psutil.disk_usage('/')
        bytes_to_gb = pow(1024, 3)
        total_disk = disk.total / bytes_to_gb
        used_disk = disk.used / bytes_to_gb
        percentage_disk = disk.percent

        if percentage_disk > 80:
            return f"Warning: Penggunaan disk di atas {percentage_disk:.2f}%\nRemaining Storage: {used_disk:.2f} GB dari {total_disk:.2f} GB."
        
        return f"Total Disk (Storage): {total_disk:.2f} GB\nUsed Disk (Storage): {used_disk:.2f} GB\nPercentage: {percentage_disk:.2f}%"
        
    except Exception:
        print(f"Error: Sistem gagal mengakses data process.")

# Tulis check_process() — function ini harus terima nama proses sebagai input, 
# cek apakah proses itu lagi jalan, dan return pesan yang sesuai: ketemu atau tidak ketemu.

def check_process(running_process):
    try:
        if running_process == None:
            raise Exception("Your input is empty!")
        for proc in psutil.process_iter(['pid', 'name']):
            if running_process == proc.info['name']:
                return f"Found: {proc.info['name']} is running!"
        return f"System Process: System process not found!"
    except Exception as e:
        print(e)

# Input user ke running_process

def input_user():
    try:
        process_input = input("Enter system process that you want to check: ")
        if process_input == "":
            raise Exception("Your input is empty!")
        while process_input:
            if process_input.isnumeric():
                return f"Your input can't be number!"
            elif process_input == None:
                raise Exception("Your input is empty!")
            return process_input       
    except Exception as e:
        print(e)

