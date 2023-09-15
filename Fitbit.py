import sys


# Reads file and returns a list of line in string format
def read_data(file_name):
    with open(file_name, "r") as f:
        data_fitbit = f.read().splitlines()
        new_data_fitbit = []
        for i in data_fitbit:
            if i.startswith("#"):
                pass
            else:
                new_data_fitbit.append(i)
    f.close()
    return new_data_fitbit


# Converts time to minutes passed after midnight
def generate_minutes_after_midnight(s):
    new_time = s.upper()
    hour_minute_split_index = new_time.find(".")
    hour = new_time[0: hour_minute_split_index]
    minutes = new_time[hour_minute_split_index + 1: len(new_time) - 2]
    meridian = new_time[len(new_time) - 2:]
    hour_to_minutes = int(hour) * 60

    if int(hour) == 12:
        if meridian == "AM":
            minutes_after_midnight = int(minutes)
        else:
            minutes_after_midnight = hour_to_minutes + int(minutes)
    elif meridian == "AM":
        minutes_after_midnight = hour_to_minutes + int(minutes)
    else:
        minutes_after_midnight = hour_to_minutes + int(minutes) + 720

    return minutes_after_midnight


# Converts string to triple
def convert_string_to_triple(d):
    splits = d.split(":")
    if len(splits) == 3:
        stime = splits[0]
        etime = splits[1]
        steps = splits[2]
        stime_min = generate_minutes_after_midnight(stime)
        etime_min = generate_minutes_after_midnight(etime)
        triple = (stime_min, etime_min, int(steps))
        return triple


# Converts triple t string
def convert_triple_to_string(d):
    str_time_new = ""
    for i in d[0:2]:
        if 60 < i < 720:
            hour = i // 60
            hour_str = str(hour)
            minutes = i % 60
            minutes_str = "%02d" % minutes
            meridian = "AM"
            str_time = f"{hour_str}.{minutes_str}{meridian}:"

        elif i == 720:
            hour = "12"
            minutes = "00"
            meridian = "PM"
            str_time = f"{hour}.{minutes}{meridian}:"

        elif 0 <= i < 60:
            hour = "12"
            minutes = "%02d" % i
            meridian = "AM"
            str_time = f"{hour}.{minutes}{meridian}:"

        else:
            hour = i // 60
            hour_str = str(hour)
            minutes = i % 60
            minutes_str = "%02d" % minutes
            meridian = "PM"

            if hour > 12:
                hour_new = hour - 12
                hour_new_str = str(hour_new)
                str_time = f"{hour_new_str}.{minutes_str}:{meridian}:"

            else:
                str_time = f"{hour_str}.{minutes_str}:{meridian}:"

        str_time_new = str_time_new + str_time

    return str_time_new + f"{d[2]}"


# Extracts triples and puts them in a list
def extract_data_parts(data):
    new_data = []
    for i in data:
        x = convert_string_to_triple(i)
        new_data.append(x)
    return new_data


# Removes invalid data
def remove_bad_data(data):
    new_data_remove = []
    for i in data:
        if (i[1] - i[0]) <= 0:
            x = convert_triple_to_string(i)
            print("INVALID data: " + x)
        else:
            new_data_remove.append(i)
    return new_data_remove


# Counts steps and time

def compute_stats(data):
    total_steps = 0
    total_time = 0
    for i in data:
        total_steps += i[2]
    for i in data:
        time = i[1] - i[0]
        total_time += time
    total_steps_and_time = [total_steps, total_time]

    return total_steps_and_time


def main():
    file_name = sys.argv[1:]
    fname = file_name[0]
    read_data_file = read_data(fname)
    extracted_data = extract_data_parts(read_data_file)
    refined_data = remove_bad_data(extracted_data)
    computed_results = compute_stats(refined_data)
    print(f"Total Steps = {computed_results[0]}")
    print(f"Hourly_step rate = {((computed_results[0] / computed_results[1]) * 60) // 1}")
    

main()
