"""program for question 1 part 1 FIFO"""
import csv

wait_time = 0

filename = open("processes.csv", "r")
file = csv.DictReader(filename)
pid = []
time = []
memory = []

for column in file:
    pid.append(column["Process ID"])
    time.append(column["CPU Cycles"])
    memory.append(column["Memory Requirement"])

# print(pid)
# print(time)
# print(memory)

for i, value in enumerate(time):
    wait_time += int(value)


avg_wait_time = wait_time / len(time)
print("average wait time is:" + str(avg_wait_time))
