from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, DetailView, View

from .forms import CustomerForm, CommentForm, FeedBackForm
from .models import Main, Category, Profile, Comment, FeedBack


class Genre:
    def get_category(self):
        return Category.objects.all().values('id')

class HomeView(ListView):
    model = Main
    template_name = 'base.html'


class ProfileMain(ListView):
    model = Profile
    template_name = 'base.html'

    def get_queryset(self, request):
        profile = request.user.profile
        return profile


def accountSettings(request):
    profile = request.user.profile
    form = CustomerForm(instance=profile)

    """добавление аватарки"""
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'account/profile.html', context)


class MainDetail(DetailView):
    model = Main
    slug_field = 'url'
    template_name = 'detail.html'

    def get(self, request, slug):
        form = CommentForm()
        main = Main.objects.get(url=slug)

        context = {'form':form, 'main':main}
        return render(request, 'detail.html', context)

    def post(self, request, slug):
        form = CommentForm()
        movie = Main.objects.get(url=slug)

        """Комментарии"""
        if request.method == 'POST':
            form = CommentForm(request.POST or None)
            if form.is_valid():
                content = request.POST.get('content')
                reply_id = request.POST.get('comment_id')
                comment_qs = None
                if reply_id:
                    comment_qs = Comment.objects.get(id=reply_id)
                comment = Comment.objects.create(post=movie, user=request.user, content=content, reply=comment_qs)
                comment.save()
                return HttpResponseRedirect(movie.get_absolute_url())
            else:
                form = CommentForm()

        context = {'form': form}
        return render(request, 'detail.html', context)

def FilterCategory(request, id):
    categories = Category.objects.all()
    posts = Main.objects.all().filter(category_id=id)
    context = {
        'category': categories,
        'posts': posts,
    }
    return render(request, 'category_filter.html', context)

def FilterSubCategory(request,id):
    category = Category.objects.all()
    posts = Main.objects.filter(subcategory_id=id)
    context = {
        'category':category,
        'posts':posts,
    }
    return render(request, 'category_filter.html', context)

"""Поиск"""

class Search(ListView):
    template_name = 'base.html'

    def get_queryset(self):
        return Main.objects.order_by('id').filter(
            Q(name__icontains=self.request.GET.get('q')))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context


class FeedBackFormView(View):
    def post(self, request):
        if request.method == 'POST':
            form = FeedBackForm(request.POST)
            message_name = request.POST['name']
            message_phone = request.POST['phone']
            message = request.POST['description']
            if form.is_valid():
                form.save()
                send_mail(message_name, message, message_phone, ['forxap@gmail.com'])
            return redirect('/')