# instalar biblioteca pytz
import pytz
from datetime import datetime

oslo = datetime.now(pytz.timezone('Europe/Oslo'))
saoPaulo = datetime.now(pytz.timezone('America/Sao_Paulo'))
dakar = datetime.now(pytz.timezone('Africa/Dakar'))
detroit = datetime.now(pytz.timezone('America/Detroit'))
fortaleza = datetime.now(pytz.timezone('America/Fortaleza'))

print('-'*20)
print(f'Oslo: {oslo}\
      \nSão Paulo {saoPaulo}\
      \nDakar {dakar}\
      \nDetroit {detroit}\
      \nFortaleza {fortaleza}')
print('-'*20)

