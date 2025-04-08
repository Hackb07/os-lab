import queue

def main():
    buffer = queue.Queue(maxsize=10)
    choice = 0

    while choice != 3:
        print("\n1. Produce \t 2. Consume \t 3. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            if buffer.full():
                print("\nBuffer is Full")
            else:
                try:
                    produce = int(input("\nEnter the value to produce: "))
                    buffer.put(produce)
                    print(f"Produced value: {produce}")
                except ValueError:
                    print("Please enter a valid integer.")
        elif choice == 2:
            if buffer.empty():
                print("\nBuffer is Empty")
            else:
                consume = buffer.get()
                print(f"\nThe consumed value is: {consume}")
        elif choice == 3:
            print("\nExiting...")
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
