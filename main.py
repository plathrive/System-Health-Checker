from system_health_checker import check_ram, check_disk, check_process

if __name__ == "__main__":
    print("Running system health checker:")
    print("==============================")
    process_input = input("Enter system process that you want to check: ")
    print(process_input)
    print("==============================")
    print(check_ram())
    print(check_disk())
    print(check_process(process_input))
    print("==============================")
    print("Process done!")
