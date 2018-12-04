import re
datetime_list = []

with open('d4-inputs') as txtfile:
    for line in txtfile:
        line_info = []

        datetime = line[1:17]
        line_info.append(datetime)

        info = line[19:].replace('\n', '')
        line_info.append(info)

        datetime_list.append(line_info)


datetime_list.sort(key=lambda x: x[0])

pattern = '#[0-9]{1,6}'

guard_profile = {}

for dt in datetime_list:
    if 'Guard' in dt[1]:
        comp = re.compile(pattern)
        search = comp.findall(dt[1])

        guard = search[0]
        guard_number = guard.replace('#', '')

        if guard_number not in guard_profile.keys():
            guard_profile[guard_number] = [0, {}]

    if 'asleep' in dt[1]:
        start_time = int(dt[0][14:16])

    if 'wakes' in dt[1]:
        end_time = int(dt[0][14:16])
        time_asleep = end_time - start_time

        guard_profile[guard_number][0] = guard_profile[guard_number][0] + time_asleep

        for i in range(start_time, end_time):
            if i not in guard_profile[guard_number][1].keys():
                guard_profile[guard_number][1][i] = 1
            else:
                guard_profile[guard_number][1][i] = guard_profile[guard_number][1][i] + 1

max_sleep = 0
sleepy_guard = 0
sleepy_minute = 0
max_sleep_minute = 0

for key, val in guard_profile.items():
    if val[0] > max_sleep:
        max_sleep = val[0]
        sleepy_guard = key

        for k, v in val[1].items():
            if v > max_sleep_minute:
                max_sleep_minute = v
                sleepy_minute = k

print(int(sleepy_guard) * int(sleepy_minute))