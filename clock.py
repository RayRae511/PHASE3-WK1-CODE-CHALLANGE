def time_converter(hour, minute, period):
    #Converting hour to 24hour format
    if period == 'am':
        if hour == 12:
            hour = 0
        else:
            if hour != 12:
                hour += 12
    # Convert hour and minute to string with leading zeros
    hour_str = str(hour).zfill(2)
    minute_str = str(minute).zfill(2)
    
    #Combining hour and minute strings
    time_string = hour_str + ':' + minute_str
    return time_string

#Testing the function...

print(time_converter(12, 10, 'am'))

