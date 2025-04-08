# 💻 Operating Systems Lab - Python Programs

This repository contains Python implementations of fundamental Operating System concepts typically covered in lab sessions. Each program demonstrates a specific OS principle such as scheduling, inter-process communication, synchronization, deadlock handling, and memory management.

---

## ✅ Programs with Explanations

### 1. FCFS Scheduling (First Come First Serve)
**Description**: Simulates FCFS scheduling where the process that arrives first is executed first.
- **Inputs**: Number of processes, Burst time for each process
- **Outputs**: Waiting time, Turnaround time for each process, Average WT and TAT
- **Explanation**: It computes the waiting time for each process based on the completion time of previous processes.

---

### 2. SJF Scheduling (Shortest Job First)
**Description**: Simulates non-preemptive SJF where processes are sorted based on burst time.
- **Inputs**: Burst times
- **Outputs**: Sorted waiting time and turnaround time for each process
- **Explanation**: Shortest burst time gets executed first, reducing overall turnaround and waiting time.

---

### 3. Round Robin Scheduling
**Description**: Simulates time-sliced Round Robin CPU scheduling.
- **Inputs**: Burst times, Time quantum (time slice)
- **Outputs**: Individual and average waiting and turnaround times
- **Explanation**: Each process gets executed in a circular order for a fixed time until it completes.

---

### 4. Priority Scheduling
**Description**: Implements scheduling based on process priority.
- **Inputs**: Priority and burst time for each process
- **Outputs**: Waiting and turnaround time for each process
- **Explanation**: Higher-priority processes are executed first. Lower priority value means higher priority.

---

### 5. Inter-Process Communication (Pipe)
**Description**: Demonstrates IPC using pipe mechanism between parent and child.
- **Inputs**: Message to be passed
- **Outputs**: Message received by the parent
- **Explanation**: A child writes to a pipe and the parent reads from it using `os.pipe()`.

---

### 6. Producer-Consumer (Bounded Buffer)
**Description**: Solves the producer-consumer problem using a bounded queue.
- **Inputs**: User choice to produce or consume
- **Outputs**: Queue state after each operation
- **Explanation**: Uses `queue.Queue()` to handle buffer overflow/underflow conditions.

---

### 7. Dining Philosophers Problem
**Description**: Classic synchronization problem using threads and locks.
- **Explanation**: Philosophers alternate between thinking and eating, sharing chopsticks (resources), while avoiding deadlocks.

---

### 8. Banker's Algorithm
**Description**: Deadlock avoidance algorithm that ensures the system stays in a safe state.
- **Inputs**: Maximum resource vector, Allocation matrix, Max claim matrix
- **Outputs**: Safe or unsafe execution sequence
- **Explanation**: It checks if available resources can satisfy the need of all processes without causing deadlock.

---

### 9. Thread Creation and ID Comparison
**Description**: Creates two threads and identifies them.
- **Explanation**: Simulates thread execution and identifies which thread is currently running by comparing thread IDs.

---

### 10. Paging and Address Translation
**Description**: Implements logical to physical address translation.
- **Inputs**: Page table, Logical address (page number and offset)
- **Outputs**: Physical address
- **Explanation**: Maps the logical address to a physical frame using the page table.

---

## 🔄 How to Run
Make sure Python 3 is installed. Then run any script:
```bash
python3 filename.py
```

---

## 👤 Author
**Tharun Bala**  
B.Tech AI & DS, 2nd Year @ PMC Tech  


---

Happy Coding ✨

