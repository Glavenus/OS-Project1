"""Round robin algorithms for waiting time and shortest turnaround time"""


def rr_wait_time(processes, n, burst_t, wait_t, quantum):

    burst_time_left = [0] * n

    for i in range(n):
        burst_time_left[i] = burst_t[i]

    t = 0

    while 1:
        done = True

        for i in range(n):

            if burst_time_left[i] > 0:
                done = False

                if burst_time_left[i] > quantum:

                    t += quantum

                    burst_time_left[i] -= quantum

                else:

                    t = t + burst_time_left[i]

                    wait_t[i] = t - burst_t[i]

                    burst_time_left[i] = 0

        if done == True:
            break


def rr_turnaround_time(processes, n, burst_t, wait_t, turnaround_t):

    for i in range(n):
        turnaround_t[i] = burst_t[i] - wait_t[i]
