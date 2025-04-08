def main():
    n = int(input("Enter the number of processes: "))
    p = list(range(1, n + 1))
    bt = [0] * n        # Burst times (will be updated during execution)
    bt1 = [0] * n       # Original burst times (for calculating waiting time later)
    tat = [0] * n       # Turnaround times

    print("Enter the burst time of each process:")
    for i in range(n):
        bt[i] = int(input(f"Process {i + 1}: "))
        bt1[i] = bt[i]

    ts = int(input("Enter the time slice (quantum): "))
    tbt = sum(bt)       # Total burst time remaining
    et = [0]            # Execution time tracker

    # Round Robin Loop
    while tbt > 0:
        for i in range(n):
            if bt[i] > 0:
                if bt[i] > ts:
                    et.append(et[-1] + ts)
                    bt[i] -= ts
                    tbt -= ts
                else:
                    et.append(et[-1] + bt[i])
                    tbt -= bt[i]
                    bt[i] = 0
                    tat[i] = et[-1]  # Store the time process ends

    wt = [tat[i] - bt1[i] for i in range(n)]  # Waiting time = TAT - BT
    awt = sum(wt) / n
    atat = sum(tat) / n

    print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{p[i]}\t{bt1[i]}\t\t{wt[i]}\t\t{tat[i]}")

    print(f"\nAverage waiting time: {awt:.2f}")
    print(f"Average turnaround time: {atat:.2f}")

if __name__ == "__main__":
    main()
