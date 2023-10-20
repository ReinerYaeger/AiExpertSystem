from pyswip import Prolog

prolog = Prolog()
prolog.consult("prolog/knowledge_base.pl")

print(prolog.query(list("parent_of('Mark',_)")))

def generate_gpa():
    gpa = [1]
    return gpa



