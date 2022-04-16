# Домашняя работа - 10.
import json
from flask import Flask

with open('candidates.json', 'r', encoding='utf8') as file:
    candidat = json.load(file)

app = Flask(__name__)


@app.route("/")
def page_index():
    all_candidates = ''
    for i in range(len(candidat)):
        one_candidat = f'''<pre>
   Имя кандидата - {candidat[i]['name']}
   Позиция кандидата - {candidat[i]['position']}
   Навыки - {candidat[i]['skills']}\n
   <pre>
   '''
        all_candidates = all_candidates + one_candidat
    return all_candidates


@app.route("/candidates/<int:x>")
def page_candidates(x):
    one_candidat = f'''
   <img src = "{candidat[x - 1]['picture']}">
   
   <pre>
   Имя кандидата - {candidat[x - 1]['name']}
   Позиция кандидата - {candidat[x - 1]['position']}
   Навыки - {candidat[x - 1]['skills']}\n
   <pre>
   '''
    return one_candidat


@app.route("/skills/<skill>")
def page_skills(skill):
    skill_candidates = ''
    for i in range(len(candidat)):
        one_candidat = f'''<pre>
      Имя кандидата - {candidat[i]['name']}
      Позиция кандидата - {candidat[i]['position']}
      Навыки - {candidat[i]['skills']}\n
      <pre>
      '''
        if skill.lower() in candidat[i]['skills'].lower().split(', '):
            skill_candidates = skill_candidates + one_candidat
    return skill_candidates


app.run()
