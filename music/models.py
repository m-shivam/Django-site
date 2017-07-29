from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

# Create your models here.
def validate(val):
    if not (str(val).endswith('.jpg') | str(val).endswith('.jpeg') | str(val).endswith('.png')):
        raise ValidationError(
            _("Selected image is not valid to use as logo. Select only jpg files."),
                              params={'value': val})

def valSong(val):
    if not (str(val).endswith('.mp3') | str(val).endswith('.m4a')):
        raise ValidationError(
            _("Selected song is not valid to in valid format. Select only .mp3 or .m4a files."),
                              params={'value': val})


class Album(models.Model):#to create your own database override models.model
    title=models.CharField(max_length=50)
    genre=models.CharField(max_length=30)
    artist=models.CharField(max_length=50)
    album_logo=models.ImageField(validators=[validate])

    def __str__(self):
        return "Album:"+self.title+" Artist:"+self.artist
    #def get_absolute_url(self):
    #    return reverse('music:album',kwargs={'pk':self.pk})

class Song(models.Model):
    alb_id=models.ForeignKey(Album,on_delete=models.CASCADE)
    stitle=models.CharField(max_length=500)
    sartist=models.CharField(max_length=20)
    fav=models.BooleanField(default=False)
    ssize=models.CharField(max_length=15,default='')
    slength=models.CharField(max_length=10,default='')
    sbitrate=models.CharField(max_length=20,default='320 kbps')
    sfile = models.FileField(validators=[valSong])

    def __str__(self):
        return "Song:"+self.stitle+" Artist:"+self.sartist