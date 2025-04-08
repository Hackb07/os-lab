def main():
    n = int(input("Enter the number of processes: "))
    p = list(range(n))  # Process indices
    bt = [0] * n        # Burst times
    pr = [0] * n        # Priorities
    wt = [0] * n        # Waiting times
    tat = [0] * n       # Turnaround times

    for i in range(n):
        pr[i] = int(input(f"Enter the priority of process {i + 1} (lower number = higher priority): "))
        bt[i] = int(input(f"Enter the burst time of process {i + 1}: "))

    # Sort by priority (ascending)
    pr, bt, p = zip(*sorted(zip(pr, bt, p)))

    wt[0] = 0
    for i in range(1, n):
        wt[i] = wt[i - 1] + bt[i - 1]

    for i in range(n):
        tat[i] = wt[i] + bt[i]

    awt = sum(wt) / n
    atat = sum(tat) / n

    print("\nProcess\tPriority\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{p[i] + 1}\t{pr[i]}\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")

    print(f"\nThe average waiting time is: {awt:.2f}")
    print(f"The average turnaround time is: {atat:.2f}")

if __name__ == "__main__":
    main()
