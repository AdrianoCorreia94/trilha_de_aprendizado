from datetime import date, datetime, time 

# criando data 
data = date(2025, 1, 15)
print(data)


# criando data e hora 
tempo = datetime(2025, 2, 12, 16, 28)
print(tempo)

hoje = datetime.today()
print(hoje)

dia_hoje = hoje.day
print(dia_hoje)

t = datetime(2025, 2, 12)

n = t.day

hora = time(9, 32, 12)
print(hora)