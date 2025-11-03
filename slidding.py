import time
import random

def sliding_window(frames, window_size):
    print("Sliding Window Protocol Simulation")
    print(f"Total Frames: {frames}")
    print(f"Window Size: {window_size}\n")
    sent = 0
    while sent < frames:
        for i in range(window_size):
            if sent + i < frames:
                print(f"Frame {sent + i + 1} sent.")
                time.sleep(0.3)
        print()
        for i in range(window_size):
            if sent >= frames:
                break
            ack = random.choice([True, True, True, False])  
            if ack:
                print(f"ACK received for Frame {sent + 1}")
                sent += 1
            else:
                print(f"ACK lost for Frame {sent + 1}! Resending window...")
                break
        print("-" * 40)
        time.sleep(0.5)
    print("\nAll frames transmitted successfully")

n = int(input("Enter total number of frames: "))
w = int(input("Enter window size: "))
sliding_window(n, w)
