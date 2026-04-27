from system_health_checker import check_ram, check_disk, check_process, input_user

if __name__ == "__main__":
    print("Running system health checker:")
    print("==============================")
    process_input = input_user()
    print("==============================")
    print(check_ram())
    print(check_disk())

    if process_input == "Your input is empty!":
        print("System Process: Your input is empty!")
    elif process_input == "Your input can't be number!":
        print("System Process: Your input can't be number!")
    else:
        print(check_process(process_input))

    print("==============================")
    print("Process done!")
