from django.contrib import admin
from newsapp.models import CategoryModel, PostModel, CommentModel

admin.site.register(CategoryModel)
admin.site.register(PostModel)
admin.site.register(CommentModel)
# Register your models here.
