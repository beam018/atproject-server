from django.contrib import admin
import reversion
from posts.models import Post, PostType, PostPlace


class PostAdmin(reversion.VersionAdmin):
  pass


class PostTypeAdmin(reversion.VersionAdmin):
  pass


class PostPlaceAdmin(reversion.VersionAdmin):
  pass


admin.site.register(Post, PostAdmin)
admin.site.register(PostType, PostTypeAdmin)
admin.site.register(PostPlace, PostPlaceAdmin)
