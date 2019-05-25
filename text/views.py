from django.shortcuts import render , redirect
from django.utils import timezone
from .models import Text , Profile
from .forms import PostForm 

def forum_page(request):
	texts = Text.objects.filter(date__lte=timezone.now()).order_by('date')
	if request.method == "POST":
		form=PostForm(request.POST)
		if form.is_valid():
			text= form.save(commit=False)
			text.author = request.user
			text.date = timezone.now()
			text.save()
			form=PostForm()
			return redirect('forum_page')
	else:
		form=PostForm()
	return render(request,'text/forum_page.html',{'texts': texts , 'form' :form})
