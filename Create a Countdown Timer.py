import time


def countdown_timer(seconds):
    while seconds > 0:
        print(f"Time left: {seconds} seconds", end='\r')
        time.sleep(1)
        seconds -= 1

    print("Time's up!")


# Example usage:
if __name__ == "__main__":
    seconds = 10  # Change this to set the countdown time in seconds
    countdown_timer(seconds)
