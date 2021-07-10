from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q



from .models import *
from .utils import *
from .forms import PostForm


def posts_list(request):
    cats = Category.objects.all()
    posts = Post.objects.all()
    cards = Post.objects.all()
    dishes = ViewDish.objects.all()
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 3)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url,
        'title': "Рецепты",
        'posts': posts, 
        'cats': cats,
        'cat_selected': 0,
        'cards': 'cards',
        'dishes': dishes,
        'dish_selected' :0,
    }

    return render(request, 'blog/categories.html', context=context)

def index(request):
    return render(request, 'blog/index.html', {'title': 'KASHEVAR'})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'



class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create_form.html'
    raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'
    raise_exception = True

class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'receipts_list_urls'
    raise_exception = True


def show_category(request, cat_id):
    posts = Post.objects.filter(cat_id=cat_id)
    print(posts, cat_id)

    cats = Category.objects.all()

    context = {
        'posts': posts,
        'title': "Рецепты",
        'cats': cats,
        'cat_selected': cat_id,
    }
    return render(request, 'blog/categories.html', context=context)

def show_dish(request, dish_id):
    posts = Post.objects.filter(dish_id=dish_id)
    cards = Post.objects.filter(dish_id=dish_id)
    print(cards, dish_id)

    dishes = ViewDish.objects.all()

    context = {
        'posts': posts,
        'cards': cards,
        'dishes': dishes,
        'dish_selected': dish_id,
    }
    return render(request, 'blog/categories.html', context=context)

def show_reviews(request):

    commentaries = Commentaries.objects.all()

    context = {
        'commentaries' : commentaries,
    }
    return render(request, 'blog/reviews.html', context=context)
