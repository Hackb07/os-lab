def main():
    n = int(input("\nEnter the number of pages in memory: "))
    ps = int(input("Enter page size: "))
    f = int(input("Enter the number of frames: "))

    page = [-1] * n  # Page table

    print("\nEnter the page table")
    print("(Enter frame number as -1 if that page is not present in any frame)\n")
    print("PageNo\tFrameNo")
    for i in range(n):
        page[i] = int(input(f"{i}\t\t"))

    while True:
        try:
            pno, off = map(int, input("\nEnter the logical address (page no & offset): ").split())
            
            if pno >= n or pno < 0:
                print("Invalid page number.")
            elif off >= ps or off < 0:
                print("Invalid offset. It should be less than page size.")
            elif page[pno] == -1:
                print("The required page is not available in any of the frames.")
            else:
                frame_no = page[pno]
                physical_addr = frame_no * ps + off
                print(f"Physical address (Frame No: {frame_no}, Offset: {off}) = {physical_addr}")
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
        
        choice = input("\nDo you want to continue (y/n)?: ").lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    main()
