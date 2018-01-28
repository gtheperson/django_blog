# forms for blog
from django import forms
from .models import Post

# gets django to import the basic idea for a ModelForm
class PostForm(forms.ModelForm):
	# tell django which model our form is based on and whih fields are to be in the form
	class Meta:
		model = Post
		fields = ('title', 'text',)