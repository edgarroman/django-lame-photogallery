from django.core.management.base import BaseCommand, CommandError
from apps.gallery.models import Photo
from django.core.files import File  
from django.conf import settings

class Command(BaseCommand):
#    args = '<poll_id poll_id ...>'
    help = 'Pulls in legacy php images'

    def handle(self, *args, **options):
        print "running image image"
        
        photo_list = Photo.objects.all().order_by('id')
#        photo_list = Photo.objects.all().filter(id__gt='12400').order_by('id')
        
        for photo in photo_list:
            print 'Working on photo id %s' % photo.id
        
            orig_path = settings.MEDIA_PHOTO_PATH + "origsize/%s.jpg" % photo.id
            print 'Opening path %s' % orig_path
            f = open(orig_path, 'r')
            
            photo.filename = File(f)
            photo.save()
        
#            if photo.id > 10:
#                break;
        
        print "done"
        

