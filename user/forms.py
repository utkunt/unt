from django import forms
from django.forms import ModelForm
from article.models import Article

class LoginForm(forms.Form):
	username = forms.CharField(label = "kullanıcı adı")
	password = forms.CharField(label = "parola", widget = forms.PasswordInput)


class ArticleForm(forms.ModelForm):

	class Meta:

		model = Article
		fields = ['title', "content"]





