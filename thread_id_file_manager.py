import csv

# Writing the thread id to a csv to save it.
def write_thread_id(channel_id):
    with open("channel_id.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([channel_id])

# Reading the thread id to memory
def read_thread_id():
    with open("channel_id.csv", "r", newline='') as file:
        reader = csv.reader(file)
        thread_id = int(next(reader)[0])

    return thread_id