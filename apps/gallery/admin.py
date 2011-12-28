from django.contrib import admin
from gallery.models import User
from gallery.models import Album
from gallery.models import Photo
from gallery.models import Notification


admin.site.register(User)
#admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(Notification)

#class PhotoAdmin(admin.ModelAdmin):
#    date_hierarchy = 'datecreated'
#    list_display = ('id','title','filename','order','datecreated')
#    list_filter = ('album__title',)
#admin.site.register(Photo,PhotoAdmin)

# http://stackoverflow.com/questions/2227891/customising-django-admin-tabularinline-default-field

class PhotoInline(admin.TabularInline):
    model = Photo
    fields = ('thumb', 'title', 'photodate','datecreated', 'order')
    readonly_fields = ('thumb', 'photodate', 'datecreated',)
#    date_hierarchy = 'datecreated'
#    list_display = ('id','title','filename','order','datecreated')
#    list_filter = ('album__title',)
    sortable_field_name = 'order'

class AlbumAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('id','title','get_link','date')
    search_fields = ['title']
    inlines = [
        PhotoInline
    ]
admin.site.register(Album,AlbumAdmin)
