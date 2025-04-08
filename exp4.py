def main():
    n = int(input("Enter total number of processes (maximum 20): "))
    if n > 20:
        print("Maximum number of processes is 20.")
        return

    bt = [0] * n  # Burst Time
    wt = [0] * n  # Waiting Time
    tat = [0] * n  # Turnaround Time

    print("Enter Process Burst Time:")
    for i in range(n):
        bt[i] = int(input(f"P[{i + 1}]: "))

    # Calculate Waiting Time
    wt[0] = 0
    for i in range(1, n):
        wt[i] = wt[i - 1] + bt[i - 1]

    # Calculate Turnaround Time and Average Times
    print("\nProcess \tBurst Time \tWaiting Time \tTurnaround Time")
    avwt = 0
    avtat = 0
    for i in range(n):
        tat[i] = bt[i] + wt[i]
        avwt += wt[i]
        avtat += tat[i]
        print(f"P[{i + 1}] \t\t {bt[i]} \t\t {wt[i]} \t\t {tat[i]}")

    avwt /= n
    avtat /= n
    print(f"\nAverage Waiting Time: {avwt:.2f}")
    print(f"Average Turnaround Time: {avtat:.2f}")

if __name__ == "__main__":
    main()
