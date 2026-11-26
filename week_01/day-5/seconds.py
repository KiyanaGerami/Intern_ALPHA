seconds = int(input("enter seconds: "))
days, rest = divmod(seconds, 86400)
hour, rest = divmod(rest, 3600)
minute, rest = divmod(rest, 60)
second = rest

print(f'{days} days', f'{hour:02d}:{minute:02d}:{second:02d}')
