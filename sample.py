import sys
import datetime

time = datetime.datetime.now()

output="hi %s current time is %s" %(sys.argv[1], time)
print(output)
sys.stdout.flush()