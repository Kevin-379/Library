from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book
from .forms import SearchForm, BorrowBookForm
import datetime


def home(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			query = form.cleaned_data['query']
			return redirect('search_book', query=query)
	form = SearchForm()
	return render(request, 'library/home.html', {'form': form})


@login_required()
def borrow(request, pk):
	if request.method == 'POST':
		form = BorrowBookForm(request.POST)
		book = Book.objects.get(pk=pk)
		if form.is_valid():
			if datetime.date.today() > form.cleaned_data['borrow_till']:
				messages.error(request, "Please choose a date in future")
				return render(request, 'library/book_borrow_form.html', {'form': form, 'book': book})
			else:
				book.availability
				messages.success(request, "Please choose a date in future")
				return redirect('library_home')
	form = BorrowBookForm()
	book = Book.objects.get(pk=pk)
	return render(request, 'library/book_borrow_form.html', {'form': form, 'book': book})


def search(request, query):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			query = form.cleaned_data['query']
			results = Book.objects.filter(title__icontains=query)[0:5]
			context = {'form': form, 'results': results}
			return render(request, 'library/search.html', context=context)
	# form = SearchForm(query)
	form = SearchForm({'query': query})
	results = Book.objects.filter(title__icontains=query)[0:5]
	context = {'form': form, 'results': results}
	return render(request, 'library/search.html', context=context)


class BookCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	model = Book
	fields = [
		'title',
		'author',
		'publisher',
		'genre',
		'summary',
		'ISBN',
		'location',
		'availability',
	]

	def form_valid(self, form):
		# self.update(form)
		# form.instance.author = self.request.user
		# Book.create(name, courses_taught, rating)
		return super().form_valid(form)

	def test_func(self):
		for group in self.request.user.groups.all():
			if group.name == "librarian":
				return True
		return False


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Book
	fields = [
		'title',
		'author',
		'publisher',
		'genre',
		'summary',
		'ISBN',
		'location',
		'availability',
	]
	template_name_suffix = '_update_form'

	def form_valid(self, form):
		# form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		for group in self.request.user.groups.all():
			if group.name == "librarian":
				return True
		return False


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Book
	success_url = '/'

	def test_func(self):
		for group in self.request.user.groups.all():
			if group.name == "librarian":
				return True
		return False


class BookListView(ListView):
	model = Book
	context_object_name = "book_list"
	paginate_by = 5


class BookDetailView(DetailView):
	model = Book
