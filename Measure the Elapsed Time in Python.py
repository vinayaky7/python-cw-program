############Using time Module
import time

# Start time
start_time = time.time()

# Perform some operation or task
for i in range(1000000):
    pass

# End time
end_time = time.time()

# Elapsed time
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time} seconds")


################Using timeit Module####################################################################
# import timeit
#
# # Measure the execution time of a specific statement or code snippet
# elapsed_time = timeit.timeit("for i in range(1000000): pass", number=1)
#
# print(f"Elapsed time: {elapsed_time} seconds")
#
#
# ######Using datetime Module###############################################################
# import datetime
#
# # Start time
# start_time = datetime.datetime.now()
#
# # Perform some operation or task
# for i in range(1000000):
#     pass
#
# # End time
# end_time = datetime.datetime.now()
#
# # Elapsed time
# elapsed_time = end_time - start_time
#
# print(f"Elapsed time: {elapsed_time.total_seconds()} seconds")
