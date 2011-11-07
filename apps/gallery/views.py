from django.http import HttpResponse, HttpResponseNotFound
from gallery.models import *
from django.template import Context, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Count

def main_page(request):

#    albums_qs = Album.objects.order_by('-date').filter(published='1')[:10]
#    albums = []
#    for album in albums_qs:
#        a = album
#        if album.photo_set.count():
#            first_photo = Photo.objects.order_by('order').filter(album=album.id)[0]
#            a['thumbnail_url'] = first_photo.get_thumbnail_url
#        albums.append(a)
    albums = Album.objects.order_by('-date').filter(published='1')[:10]

    context = Context()
    context['albums'] = albums
    request_context = RequestContext(request)
    return render_to_response('homepage.html',
                              context,
                              request_context)
    
def album_list(request, page_id='0'):

    page_size = 10
    page_id = int(page_id)
    start = page_id * page_size
    end = start + page_size

    albums = Album.objects.order_by('-date').filter(published='1')[start:end]
    
    if len(albums) <= 0:
        next_page_id = None
    else:
        next_page_id = page_id + 1
    
    if page_id == 0:
        prev_page_id = None
    else:
        prev_page_id = page_id - 1

    context = Context()
    context['albums'] = albums
    context['next_page_id'] = next_page_id
    context['prev_page_id'] = prev_page_id
    request_context = RequestContext(request)
    return render_to_response('album-list.html',
                              context,
                              request_context)

def album_list_by_year(request, year=None):

    albums = Album.objects.order_by('-date').filter(published='1',date__year=year)

    context = Context()
    context['albums'] = albums
    context['next_page_id'] = None
    context['prev_page_id'] = None
    request_context = RequestContext(request)
    return render_to_response('album-list.html',
                              context,
                              request_context)

def album_list_by_year_years(request):

    album_dates = Album.objects.dates('date','year')

    context = Context()
    context['album_dates'] = album_dates
    request_context = RequestContext(request)
    return render_to_response('album-list-by-year.html',
                              context,
                              request_context)

def album_view(request, album_id=None):

    if not album_id:
        return HttpResponseNotFound('No such album')
        
    album = Album.objects.get(id=album_id)
#    photos = Photo.objects.order_by('order').filter(album=album_id)

    context = Context()
#    context['photos'] = photos
    context['album'] = album
    request_context = RequestContext(request)
    return render_to_response('album-view.html',
                              context,
                              request_context)

def photo_view(request, photo_id=None):
    
    if not photo_id:
        return HttpResponseNotFound('No such photo')

    photo = Photo.objects.get(id=photo_id)
    
    context = Context()
    context['photo'] = photo
#    context['album'] = album
    request_context = RequestContext(request)
    return render_to_response('photo-view.html',
                              context,
                              request_context)
