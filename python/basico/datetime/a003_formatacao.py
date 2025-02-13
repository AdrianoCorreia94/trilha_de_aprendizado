# metodo strftime (string format time): formatacao
from datetime import datetime 

# string format time = FORMATACAO
agora = datetime.now()

format = agora.strftime('%d/%m/%Y %h:%m')  # formatacao com h e m minusculos

format2 = agora.strftime('%d/%m/%y %H:%M') # formatacao com H e M maiusculos

personalizado = agora.strftime(f'%d de %h de %Y')


dia_semana = agora.strftime('%a %A')

print(f'SEM FORMATACAO {agora}\n')
print(f'h e m minusculo {format}\n')
print(f'h e m maiusculo {format2}\n')
print(f'Personalizado {personalizado}\n')
print(f'a minusculo {dia_semana}\n')