from django.contrib import admin
from .models import AuthorModel, BookModel, CommentsModel

admin.site.register(AuthorModel)
admin.site.register(BookModel)
admin.site.register(CommentsModel)
