def main():
    processes = int(input("\nEnter number of processes: "))
    resources = int(input("\nEnter number of resources: "))

    current = [[0] * resources for _ in range(processes)]
    maximum_claim = [[0] * resources for _ in range(processes)]
    available = [0] * resources
    allocation = [0] * resources
    maxres = [0] * resources
    running = [1] * processes

    for i in range(resources):
        maxres[i] = int(input(f"\nEnter Claim Vector for resource {i + 1}: "))

    print("\nEnter Allocated Resource Table:")
    for i in range(processes):
        for j in range(resources):
            current[i][j] = int(input(f"Process {i + 1}, Resource {j + 1}: "))

    print("\nEnter Maximum Claim Table:")
    for i in range(processes):
        for j in range(resources):
            maximum_claim[i][j] = int(input(f"Process {i + 1}, Resource {j + 1}: "))

    print("\nThe Claim Vector is:", maxres)

    print("\nThe Allocated Resource Table:")
    for i in range(processes):
        print("\t".join(map(str, current[i])))

    print("\nThe Maximum Claim Table:")
    for i in range(processes):
        print("\t".join(map(str, maximum_claim[i])))

    # Calculate allocated resources
    for i in range(processes):
        for j in range(resources):
            allocation[j] += current[i][j]

    print("\nAllocated resources:", allocation)

    for i in range(resources):
        available[i] = maxres[i] - allocation[i]

    print("\nAvailable resources:", available)

    counter = processes
    safe = False

    while counter != 0:
        safe = False
        for i in range(processes):
            if running[i]:
                exec = True
                for j in range(resources):
                    if maximum_claim[i][j] - current[i][j] > available[j]:
                        exec = False
                        break
                if exec:
                    print(f"\nProcess {i + 1} is executing.")
                    running[i] = 0
                    counter -= 1
                    safe = True
                    for j in range(resources):
                        available[j] += current[i][j]
                    break  # Check again from first process
        if not safe:
            print("\nThe processes are in an **unsafe state**.")
            break
    else:
        print("\nThe processes are in a **safe state**.")
        print("Available vector after execution:", available)

if __name__ == "__main__":
    main()
