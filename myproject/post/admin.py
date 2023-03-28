from django.contrib import admin
from django.utils import timezone
from django.utils.safestring import mark_safe

from .forms import PostForm
from .models import Post, Comment, Tag

admin.site.register(Tag)


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


def update_date(modeladmin, request, queryset):
    queryset.update(date_edit=timezone.now())


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Details', {'fields': ['tag', 'title', 'description']}),
        (None, {'fields': ['author', ('_get_image', 'image')]}),
        (None, {'fields': ['get_likes']}),
        ('Dates', {'fields': ['date_pub', 'date_edit']})
    ]
    readonly_fields = ['_get_image', 'get_likes', 'date_pub', 'date_edit']
    inlines = [CommentInline]

    list_display = ['_get_image', 'title', 'description', 'author', 'date_pub', 'date_edit']
    list_filter = ['tag', ]
    search_fields = ['author__username', 'author__first_name', 'author__last_name']

    form = PostForm

    def _get_image(self, obj):
        return mark_safe(u'<img style="width: 50px" src="%s" >' % obj.image.url)

    actions = [update_date, ]


