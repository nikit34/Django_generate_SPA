from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
import datetime
from django.views.generic.list import ListView
from hitcount.views import HitCountDetailView
from django.utils.text import slugify

from .forms import PageForm
from .models import Page, Category


def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {'count': count})


def logup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/logup.html', {'form': form})


class PageListView(ListView):
    model = Page
    context_object_name = 'pages'
    template_name = 'page_manager/page_list.html'


class PageDetailView(HitCountDetailView):
    model = Page
    context_object_name = 'page'
    template_name = 'page_manager/page_detail.html'
    slug_field = 'slug'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)
        context.update({
            'popular_pages': Page.objects.order_by('-hit_count_generic__hits')[:5],
        })
        return context


def upload_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.publish_date = datetime.datetime.now()
            form.instance.slug = slugify(datetime.datetime.now())
            form.save()
            return redirect('page_list')
    else:
        form = PageForm()
    return render(request, 'page_manager/upload_page.html', {'form': form})


def delete_page(request, pk):
    if request.method == 'POST':
        page = Page.objects.get(pk=pk)
        page.delete()
    return redirect('page_list')


def is_valid_queryparam(param):
    return param != '' and param is not None


def searchFilterView(request):
    qs = Page.objects.all()
    categories = Category.objects.all()
    title_contains_query = request.GET.get('title_contains')
    id_exact_query = request.GET.get('id_exact')
    title_or_author_query = request.GET.get('title_or_author')
    view_count_min = request.GET.get('view_count_min')
    view_count_max = request.GET.get('view_count_max')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    category = request.GET.get('category')
    reviewed = request.GET.get('reviewed')
    not_reviewed = request.GET.get('notReviewed')

    if is_valid_queryparam(title_contains_query):
        qs = qs.filter(name__icontains=title_contains_query)
    elif is_valid_queryparam(id_exact_query):
        qs = qs.filter(id=id_exact_query)
    elif is_valid_queryparam(title_or_author_query):
        qs = qs.filter(Q(name__icontains=title_or_author_query)
        | Q(author__name__icontains=title_or_author_query)).distinct()

    if is_valid_queryparam(view_count_min):
        qs = qs.filter(views__gte=view_count_min)
    if is_valid_queryparam(view_count_max):
        qs = qs.filter(views__lt=view_count_max)

    if is_valid_queryparam(date_min):
        qs = qs.filter(publish_date__gte=date_min)
    if is_valid_queryparam(date_max):
        qs = qs.filter(publish_date__lt=date_max)

    if is_valid_queryparam(category) and category != 'Выберите...':
        qs = qs.filter(category__name=category)

    if reviewed == 'on' and not_reviewed != 'on':
        qs = qs.filter(reviewed=True)
    elif reviewed != 'on' and not_reviewed == 'on':
        qs = qs.filter(reviewed=False)

    context = {
        'queryset': qs,
        'categories': categories
    }
    return render(request, 'page_manager/search.html', context)