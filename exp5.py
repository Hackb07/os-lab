import os

def main():
    fd_r, fd_w = os.pipe()  # Create pipe (fd_r = read end, fd_w = write end)

    if os.fork() == 0:
        # Child process
        os.close(fd_r)  # Close unused read end
        msg = input("Enter the string to enter into the pipe: ").encode()
        os.write(fd_w, msg)  # Write to the pipe
        os.close(fd_w)       # Close write end
        os._exit(0)
    else:
        # Parent process
        os.close(fd_w)       # Close unused write end
        r = os.fdopen(fd_r)  # Open read end as file object
        print("\nThe String retrieved from the pipe is:", r.read())
        os.close(fd_r)       # Close read end

if __name__ == "__main__":
    main()
