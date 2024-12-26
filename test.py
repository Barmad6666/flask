import itertools
import threading
import time  

def brute_force(target_password, characters, min_length=1, max_length=20):
    global stop, found_event
    stop=False
    attempts = [0]  
    found_event = threading.Event() 
    start_time = time.time()  
    def brute_force_part(length, characters, target_password, attempts, found_event):
        for password_tuple in itertools.product(characters, repeat=length):
            password = ''.join(password_tuple)
            attempts[0] += 1
            if password == target_password:
                elapsed_time = time.time() - start_time 
                print(f"Password found: {password}")
                print(f"Total attempts: {attempts[0]}")
                print(f"Time taken: {elapsed_time:.21f} seconds")  
                found_event.set() 
                return
            if found_event.is_set():
                return 
    def fps(a):
        if found_event.is_set() or stop:
            return
        time.sleep(1)
        a+=1
        print(f"running...({a})")
        fps(a)
    # Start threads for different password lengths
    threads = []
    thread = threading.Thread(target=fps,args=(0,))
    threads.append(thread)
    thread.start()
    
    for length in range(min_length, max_length + 1):
        thread = threading.Thread(target=brute_force_part, args=(length, characters, target_password, attempts, found_event))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    # If password is not found after all attempts
    if not found_event.is_set():
        stop=True
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        print(f"Password not found.")
        print(f"Time taken: {elapsed_time:.21f} seconds")  # Print elapsed time

target_password = "123456"
characters = "0123456789abcdefghijklmnopqrstuvwxyz_!£$%^&*()_+-=*`¬#~ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
brute_force(target_password, characters)
