from datetime import  datetime, timezone, timedelta

saoPaulo = datetime.now(timezone(timedelta(hours=-3)))  # sao paulo
dakar = datetime.now(timezone(timedelta(hours=0)))
oslo = datetime.now(timezone(timedelta(hours=+1)))
detroit = datetime.now(timezone(timedelta(hours=-5)))

print(f'Sao Paulo {saoPaulo}\
      \nDakar {dakar}\
      \nDetroit{detroit}')