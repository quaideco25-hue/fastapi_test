from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autoriser toutes les origines
    allow_methods=["*"],  # Autoriser toutes les méthodes HTTP
    allow_headers=["*"],  # Autoriser tous les en-têtes
)
# definir le modèle de données pour les requêtes
class student(BaseModel):
    id: int
    name: str
    grade: int

# créer une liste pour stocker les items

students = [
    student(id=1, name="Alice", grade=85),
    student(id=2, name="Bob", grade=90),
]

# endpoint pour récupérer tous les items
@app.get("/students")
def get_students():
    return students


#endpoint pour ajouer un etudiant
@app.post("/students")
def creer_etudiant(etudiant: student):
    students.append(etudiant)
    return {"message": "Etudiant ajouté avec succès", "Etudiant": etudiant}

# endpoint pour mettre à jour les informations d'un étudiant
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: student):
    for student in students:
        if student.id == student_id:
            student.name = updated_student.name
            student.grade = updated_student.grade
            return {"message": "Etudiant mis à jour avec succès", "Etudiant": student}
    return {"message": "Etudiant non trouvé"}

# endpoint pour supprimer un étudiant
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student.id == student_id:
            students.remove(student)
            return {"message": "Etudiant supprimé avec succès"}

    return {"message": "Etudiant non trouvé"}
