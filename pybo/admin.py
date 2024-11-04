from django.contrib import admin
from .models import Question, Answer

# admin.site.register(Question)
# admin.site.register(Answer)

class QuestionAdmin(admin.ModelAdmin):
  search_fields = ['subject']
class AnswerAdmin(admin.ModelAdmin):
  search_fields = ['content']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)