from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post
from .forms import PostForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.db.models import Q
from django.views import View
from django.shortcuts import render




class PostListView(ListView):
    model = Post
    template_name = 'blog/post-list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    # paginate_by = 10
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | Q(content__icontains=search_query)
            )
        return queryset

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'
    context_object_name = 'post'
    def get_object(self, queryset=None):
        # DetailView의 메서드를 오버라이드하여 조회수 증가 처리를 추가
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save()
        return obj

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post-form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post-form.html'

    def test_func(self):
        return self.get_object().author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post-confirm-delete.html'
    success_url = '/blog'
    def test_func(self):
        return self.get_object().author == self.request.user


class SignupView(FormView):
    template_name = 'blog/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('post-list')

class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html'
    success_url = reverse_lazy('post-list')

class StatsView(View):
    template_name = 'blog/stats.html'
    def get(self, request):
        stats_data = {
            'total_users': 1000,
            'total_posts': 5000,
        }

        return render(request, self.template_name, {'stats_data': stats_data})

