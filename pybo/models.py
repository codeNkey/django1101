from django.db import models

class Question(models.Model):
  subject = models.CharField(max_length=200) 
  content = models.TextField()
  create_date = models.DateTimeField()#입력시간 출력함수 장고쉘에서 create_date=timezone.now()로 활용

  def __str__(self):
    return self.subject

class Answer(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  content = models.TextField()
  create_date =models.DateTimeField()

