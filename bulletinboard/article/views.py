from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from article.models import Article
from article.forms import ArticleForm

# Create your views here.

class ArticleDashboardView(View):
    article_form = ArticleForm

    def get(self, request):
        # get method
        articles = Article.objects.all()
        # give context to forms
        context = {
            'article': articles,
            'sample': 1,
        }
        # render to dashboard
        return render(request, 'dashboard.html', context)

    def post(self, request):
        # post method (update & delete)
        article = Article.objects.get(id = request.POST.get('id')) #pylint: disable=no-member

        if 'btnUpdate' in request.POST: 
            # for update
            form = self.article_form(request.POST, request.FILES, instance=article) 
            if form.is_valid(): 
                # redirect to dashboard
                form.save() 
                return redirect('articleDashboard') 
            return HttpResponse(form.errors) 
            
        elif 'btnDelete' in request.POST:
            # for delete
            article.delete()
            # redirect to dashboard
            return redirect('articleDashboard')

class articleRegistrationView(View):
    # for registration
    article_form = ArticleForm

    def get(self, request):
        # proceed to registration form
        context = {'form' : self.article_form}
        # return to dashboard
        return render(request, 'create.html', context)

    def post(self, request):
        # validation of form
        form = self.article_form(request.POST, request.FILES)

        if form.is_valid():
            # redirect to dashboard
            form.save()
            return redirect('articleDashboard')
        
        return HttpResponse(form.errors)