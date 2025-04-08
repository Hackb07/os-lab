import threading
import time
import random

def philosopher(phil_num, chopsticks):
    left = phil_num
    right = (phil_num + 1) % 5

    while True:
        print(f"Philosopher {phil_num + 1} is thinking.")
        time.sleep(random.uniform(1, 3))

        print(f"Philosopher {phil_num + 1} is hungry.")

        # Avoid deadlock by picking up the lower-numbered chopstick first
        first, second = (left, right) if left < right else (right, left)

        chopsticks[first].acquire()
        chopsticks[second].acquire()

        print(f"Philosopher {phil_num + 1} is eating.")
        time.sleep(random.uniform(1, 3))

        chopsticks[first].release()
        chopsticks[second].release()

        print(f"Philosopher {phil_num + 1} finished eating.\n")

def main():
    chopsticks = [threading.Lock() for _ in range(5)]
    philosophers = []

    for i in range(5):
        phil = threading.Thread(target=philosopher, args=(i, chopsticks))
        philosophers.append(phil)
        phil.start()

    for phil in philosophers:
        phil.join()

if __name__ == "__main__":
    main()
