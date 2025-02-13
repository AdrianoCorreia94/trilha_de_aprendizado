# metodo strptime: string parse time 

from datetime import datetime 

agora = datetime.now()

data_hora_str = '2023-10-20 10:20'
mascara_ptbr = '%d/%m/%Y %a'
mascara_enUS = '%Y-%m-%d %H:%M'

conversao = datetime.strptime(data_hora_str, mascara_enUS)
print(conversao)