from django.shortcuts import render, get_object_or_404
from article.models import Article

# Create your views here.
def index(request):

	keyword = request.GET.get("keyword")

	if keyword:
		articles = Article.objects.filter(title__contains = keyword)
		return render(request, "index.html",{"articles":articles})

	articles = Article.objects.all()
	return render(request, "index.html",{"articles":articles})

def about(request):
	return render(request, "about.html")


def detail(request,id):
	#article = Article.objects.filter(id=id).first()
	article = get_object_or_404(Article,id=id)
	return render(request, "detail.html",{"article":article})