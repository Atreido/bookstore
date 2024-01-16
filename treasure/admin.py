from django.contrib import admin
from .models import Books, News, Comments, Categories, UserDetails, Orders
admin.site.register(Books)
admin.site.register(Categories)
admin.site.register(News)
admin.site.register(Comments)
admin.site.register(UserDetails)
admin.site.register(Orders)
