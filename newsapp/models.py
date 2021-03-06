from django.db import models

from userapp.models import UserModel

class  CategoryModel(models.Model):
    title= models.CharField(max_length=225)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'

class PostModel(models.Model):
    title= models.CharField(max_length=225)
    posted_on = models.DateTimeField(auto_now_add = True)
    posted_by = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='posts')
    context= models.TextField()
    header_image = models.ImageField(upload_to="post_uploads")
    category= models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

class CommentModel(models.Model):
    commented_on = models.DateTimeField(auto_now_add=True)
    commented_by = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='comments')
    context=models.TextField()
    parent_post=models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        verbose_name_plural = 'Comments'


    def __str__(self):
        return self.context
