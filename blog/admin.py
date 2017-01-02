from django.contrib import admin
from .models import Post,Category,Composer,Label

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Composer)
admin.site.register(Label)

# Register your models here.
