import random
import time
import threading

def write_random_number_to_file(filename):
    random_number = random.randint(1, 100)

    time.sleep(1)

    with open(filename, 'w') as file:
        file.write(str(random_number))

def run_functions_sequentially():
    start_time = time.time()
    
    for i in range(1000):
        write_random_number_to_file(f'file_{i}.txt')

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Sequential Execution Time: {elapsed_time} seconds")

def run_functions_multithreaded():
    start_time = time.time()
    threads = []

    for i in range(1000):
        thread = threading.Thread(target=write_random_number_to_file, args=(f'file_{i}.txt',))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Multithreaded Execution Time: {elapsed_time} seconds")

if __name__ == "__main__":
    run_functions_sequentially()
    run_functions_multithreaded()
