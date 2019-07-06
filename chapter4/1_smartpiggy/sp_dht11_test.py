import sp_dht11 as dht11
import datetime
import time
try:

	while True:
		 dt = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
		 fmt = "{0} temp : {1[1]}℃  / {1[0]}%"

		 print(fmt.format(dt, dht11.get_humidity_temperature()))

		 time.sleep(3)

except KeyboardInterrupt:
	 print("finished")

