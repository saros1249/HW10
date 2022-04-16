# Домашняя работа - 10.
from flask import Flask
from utils import candidates, get_candidat

app = Flask(__name__)


@app.route("/")
def page_index():
    candidat = candidates()
    all_candidates = ''
    for i in range(len(candidat)):
        one_candidat = get_candidat(i)
        all_candidates = all_candidates + one_candidat
    return all_candidates


@app.route("/candidates/<int:x>")
def page_candidates(x):
    candidat = candidates()
    one_candidat = f'''
   <img src = "{candidat[x - 1]['picture']}">
   
   <pre>
   one_candidat = {get_candidat(x - 1)}
   '''
    return one_candidat


@app.route("/skills/<skill>")
def page_skills(skill):
    candidat = candidates()
    skill_candidates = ''
    for i in range(len(candidat)):
        one_candidat = get_candidat(i)
        if skill.lower() in candidat[i]['skills'].lower().split(', '):
            skill_candidates = skill_candidates + one_candidat
    return skill_candidates


app.run()
