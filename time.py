import time

def main():
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min

    if hour >= 7:
        print("Es hora de ir a casa.")
    else:
        time_left = (7 - hour - 1) * 60 + (60 - minute)
        print(f"Quedan {time_left} minutos de trabajo.")

if __name__ == "__main__":
    main()
