import json
from datetime import datetime

def read_programacao():
	with open('programacao.json') as json_data:
	    programacao = json.load(json_data)

	now = datetime.now()

	for p in programacao:

		str_date = now.strftime("%d %m %y ") + p['time']
		hora_p = datetime.strptime(str_date,'%d %m %y %H:%M')
		dif_tempo =  (now - hora_p).total_seconds()
		if dif_tempo < 0:
			programa_proximo = p
			break

	return p

