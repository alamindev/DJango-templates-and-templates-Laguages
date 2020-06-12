from django.shortcuts import render, HttpResponse
from drfapp.models import Article

def get_article(request):
	
	return render(request, 'home_page.html')
   
 



def test_template(request):
	queryset = Article.objects.all()
	context = {
	  "var1":None,
	  "var2":None,
	  "queryset":queryset

	}
	return render(request, 'article_update.html', context)





def home(request):
	blog = Article.objects.all()
	context ={
	   'blog':blog,
	}
	return render(request, "tutorial/home.html", context)


def about(request):
	return render(request, "tutorial/about.html", {"title":'About'})

	# filter_backends = [SearchFilter]
	# search_fields = ['content', 'created_by__first_name']

	# def get_queryset(self, *args, **kwargs):
	# 	queryset  = Article.objects.all()
	# 	query  = self.request.GET.get('q')
	# 	if query:
	# 		queryset=queryset.filter(
 #                Q(content__icontains=query)
	# 			).distinct()

	# 	return queryset


	# def get_queryset(self):
	# 	return Article.objects.filter(created_by=self.request.user)

	
   
    # Filtering against the URL
	# def get_queryset(self):
	# 	username = self.kwargs['username']
	# 	return Article.objects.filter(created_by=username)
	#  