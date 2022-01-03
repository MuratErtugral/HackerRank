def count_substring(string, sub_string):
    count = 0
    for m in range(len(string)):
        if string[m:].startswith(sub_string):
            count += 1
    return (count)

