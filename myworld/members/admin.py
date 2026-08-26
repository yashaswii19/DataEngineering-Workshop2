from django.contrib import admin

from .models import Blog, Students


class DjStudentAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "address",
        "roll_number",
        "mobile",
        "branch",
    )
    list_filter = ("branch",)


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "release_date", "blog_time", "created_date")
    list_filter = ("author",)


# Register your models here.
admin.site.register(Students, DjStudentAdmin)
admin.site.register(Blog, BlogAdmin)
