from django.forms import ModelForm
from .models import Candidate, Position, Vote

class QuestionModelForm(ModelForm):
    class Meta:
        model = Candidate
        #fields =['question_text', 'pub_date']
        #include = []
        exclude = ['id']


class QuestionModelForm1(ModelForm):
    class Meta:
        model = Position
        exclude = ['id']
        #include = []


class QuestionModelForm1(ModelForm):
    class Meta:
        model = Vote
        exclude = ['id']
        #include = []
