# from django import forms

# from .models import QuestionAttempt

# class UserAttemptForm(forms.ModelForm):

# 	class Meta:
# 		model = QuestionAttempt
# 		fields = ('user', 'question' , 'answer', 'correctAnswer' , 'isCorrectAnswer', 'submit_date')

# 	def __init__(self, user, *args, **kwargs):
# 		self.user = user
# 		super(UserAttemptForm, self).__init__(*args, **kwargs)

# 	def save(self):
# 		attempt = super(UserAttemptForm, self).save(commit=False)
# 		attempt.user = self.user
# 		attempt.save()
# 		return attempt
