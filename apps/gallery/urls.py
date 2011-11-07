from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('apps.gallery.views',
    url(r'^$', 'main_page', name='home'),
    url(r'^albums/page/(?P<page_id>\d+)/$', 'album_list', name='album-list'),
    url(r'^album/(?P<album_id>\d+)/$', 'album_view', name='album-view'),
    url(r'^photo/(?P<photo_id>\d+)/$', 'photo_view', name='photo-view'),
    url(r'^album-list-by-year/$', 'album_list_by_year_years', name='album-list-by-year-years'),
    url(r'^album-list-by-year/(?P<year>\d+)/$', 'album_list_by_year', name='album-list-by-year'),    

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),

)
