"""SFJ algorithms for q1 part 3"""


def sjf_turnaround_time(processes, n, wait_t, turnaround_t):

    for i in range(n):
        turnaround_t[i] = processes[i][1] + wait_t[i]
