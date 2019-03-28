import time

start = time.mktime(time.strptime("%s 00:00:00" % time.strftime("%Y-%m-%d", time.localtime(time.time() - 24 * 60 * 60)),
                                  "%Y-%m-%d %H:%M:%S"))
end = int(start) + 24 * 60 * 60 - 1
