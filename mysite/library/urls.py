from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='library_home'),
	path('book/', views.BookListView.as_view(), name='book_list'),
	path('book/new/', views.BookCreateView.as_view(), name='book_create'),
	path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
	path('search/book/<str:query>/', views.search, name='search_book'),
	path('book/<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
	path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
	path('book/<int:pk>/borrow/', views.borrow, name='book_borrow'),
]
