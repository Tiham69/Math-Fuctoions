from datetime import timedelta, timezone, datetime

n = datetime.now()
t = datetime.today()
u = datetime.utcnow()

print(f'{n} -- {t} -- {u}')

a = timedelta(days= 1)
print(a)
b = timedelta(hours= 1)
print(b)

c = a - b
print(c)

min_6 = timezone(timedelta(hours= -6))
plus_6 = timezone(timedelta(hours= 6))

d = datetime.now(min_6)
print(f'{min_6} : {d.astimezone(min_6)}')
print(f'{timezone.utc} : {d.astimezone(timezone.utc)}')
print(f'{plus_6} : {d.astimezone(plus_6)}')

date_sys = d.astimezone()
print(f'{date_sys.tzinfo} : {date_sys}')