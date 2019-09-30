from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^authors$', views.authors),
    url(r'^books/(?P<get_id>\d+)$', views.books),
    url(r'^authors/(?P<get_id>\d+)$', views.authorsview),
    url(r'^new_book$', views.new),
    url(r'^new_author$', views.newa),
    url(r'^book_add/(?P<get_id>\d+)$', views.addbook_to_author),
    url(r'^author_add/(?P<get_id>\d+)$', views.addauthor_to_book),

]