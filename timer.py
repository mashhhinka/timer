import time

def countdown_timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds

    while total_seconds >= 0:
        h = total_seconds // 3600
        m = (total_seconds % 3600) // 60
        s = total_seconds % 60

        print(f"{h:02d}:{m:02d}:{s:02d}")
        time.sleep(1)
        total_seconds -= 1

    print("Time's up!")

def main():
    user_input = input("Insert time to count down (h:m:s): ")

    try:
        h, m, s = map(int, user_input.split(":"))
        countdown_timer(h, m, s)
    except ValueError:
        print("Invalid format! Please use h:m:s")

if __name__ == "__main__":
    main()
