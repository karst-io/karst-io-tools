
def dms_to_dd(dms):
	hour = float(dms[0:2])
	minutes = float(dms[2:4])
	seconds = float(dms[4:6])
	return (hour + (minutes/60) + (seconds/3600))