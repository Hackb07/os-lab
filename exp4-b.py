def main():
    n = int(input("Enter the number of processes: "))
    p = list(range(1, n + 1))  # Process IDs
    bt = [0] * n  # Burst Time
    wt = [0] * n  # Waiting Time
    tat = [0] * n  # Turnaround Time

    print("Enter the burst time of processes:")
    for i in range(n):
        bt[i] = int(input(f"Process {i + 1}: "))

    # Sort the processes based on burst time (SJF)
    bt, p = zip(*sorted(zip(bt, p)))  # Sort both burst time and process IDs

    wt[0] = 0
    for i in range(1, n):
        wt[i] = wt[i - 1] + bt[i - 1]

    for i in range(n):
        tat[i] = wt[i] + bt[i]

    twt = sum(wt)
    ttat = sum(tat)
    awt = twt / n
    atat = ttat / n

    print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{p[i]}\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")

    print(f"\nThe average waiting time is: {awt:.2f}")
    print(f"The average turnaround time is: {atat:.2f}")

if __name__ == "__main__":
    main()
