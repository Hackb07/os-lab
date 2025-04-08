import threading
import time

def do_some_thing(thread_num):
    thread_id = threading.current_thread().ident
    print(f"\nThread {thread_num + 1} (ID: {thread_id}) is processing...")
    
    # Simulate workload
    for _ in range(10**6):
        pass

def main():
    threads = []

    for i in range(2):
        t = threading.Thread(target=do_some_thing, args=(i,))
        threads.append(t)
        t.start()

    print("\nThreads created successfully.")

    # Join threads to wait for completion
    for t in threads:
        t.join()

    print("\nAll threads have completed execution.")

if __name__ == "__main__":
    main()
