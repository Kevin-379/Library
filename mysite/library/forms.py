from django import forms


class SearchForm(forms.Form):
	query = forms.CharField(label='query', max_length=20)


class BorrowBookForm(forms.Form):
	borrow_till = forms.DateField(label='borrow_till')
