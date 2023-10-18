from ai_expert_system.models import StudentMaster
from django.forms import ModelForm

class StudentForm(ModelForm):
    class Meta:
        model = StudentMaster
        fields=["student_id","student_name","student_email","school","programme"]
