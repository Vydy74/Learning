import datetime
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            all_data.append(line)

if __name__ == "__main__":
    filenames = [f"./file {number}.txt" for number in range(1, 5)]

    start_time = datetime.datetime.now()
    for filename in filenames:
        read_info(filename)
    end_time = datetime.datetime.now()
    print(f"Linear: {end_time - start_time} seconds")

    start_time = datetime.datetime.now()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    end_time = datetime.datetime.now()
    print(f"Multiprocessing: {end_time - start_time} seconds")