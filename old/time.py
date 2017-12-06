import datetime
#nah
try:
    while True:
        current_time = datetime.datetime.time(datetime.datetime.now())
        print('\b' * str(current_time), end='', flush=True)

except KeyboardInterrupt:
    print("\nDone.")
