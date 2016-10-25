from datetime import timedelta as timedelta

def	format_output_timedelta(duration_timedelta):
	hours, remainder = divmod(duration_timedelta, 3600)
	minutes, seconds = divmod(remainder, 60)
	return (hours, minutes)


def main():
	t = timedelta()
	with open("42_hour", "r") as file:
		l = file.read().splitlines()
	for x in l:
		t += timedelta(hours = int(x[:2]), minutes = int(x[3:]))
	(h, m) = format_output_timedelta(t.days * 86400 + t.seconds)
	print '%d:%02d' % (h, m)

main()
