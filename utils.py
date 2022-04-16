import json


def candidates():
    with open('candidates.json', 'r', encoding='utf8') as file:
        candidat = json.load(file)
    return candidat


def get_candidat(numder):
    candidat = candidates()
    one_candidat = f'''<pre>
       <h1>Имя кандидата - {candidat[numder]['name']}
       Позиция кандидата - {candidat[numder]['position']}
       Навыки - {candidat[numder]['skills']}\n</h1>
       <pre>
       '''
    return one_candidat
