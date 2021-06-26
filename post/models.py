from django.db import models
from django.contrib.auth.models import User
from numpy.lib.utils import source
from .feature import FeatureExtractor
from PIL import Image

from pathlib import Path
import numpy as np

class NumpyImage():
    def __init__(self, source=None):
        fe = FeatureExtractor()
        feature = fe.extract(img=source.open())
        feature_path = Path("./media/feature") / ("xxx.npy")  # e.g., ./static/feature/xxx.npy
        np.save(feature_path, feature)

        

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class Post(models.Model):
    post_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    CAT = (
        ('Elektronika', 'Elektronika'),
        ('Avtomobil', 'Avtomobil'),
        ('Daşınmaz əmlak', 'Daşınmaz əmlak')
    )

    cat = models.CharField(max_length=100, choices=CAT)
    title = models.CharField(max_length=100)

    SEH = (
        ('Ağdam', 'Ağdam'),
        ('Ağdaş', 'Ağdaş'),
        ('Agcabedi', 'Agcabedi'),   
        ('Ağstafa', 'Ağstafa'),
        ('Astara', 'Astara'),
        ('Ağsu', 'Ağsu'),
        ('Bakı', 'Bakı'),
        ('Balakən', 'Balakən'),
        ('Beyləqan', 'Beyləqan'),
        ('Bərdə', 'Bərdə'),
        ('Biləsuvar', 'Biləsuvar'),
        ('Cəbrayıl', 'Cəbrayıl'),
        ('Cəliləbad', 'Cəliləbad'),
        ('Culfa', 'Culfa'),
        ('Daşkəsən', 'Daşkəsən'),
        ('Dəliməmmədli', 'Dəliməmmədli'),
        ('Füzuli', 'Füzuli'),
        ('Gədəbəy', 'Gədəbəy'),
        ('Gəncə', 'Gəncə'),
        ('Goranboy', 'Goranboy'),
        ('Göyçay', 'Göyçay'),
        ('Hacıqabul', 'Hacıqabul'),
        ('İmişli', 'İmişli'),
        ('İsmayıllı', 'İsmayıllı'),
        ('Kürdəmir', 'Kürdəmir'),
        ('Lerik', 'Lerik'),
        ('Lənkəran', 'Lənkəran'),       
        ('Masallı', 'Masallı'),
        ('Mingəçəvir', 'Mingəçəvir'),
        ('Naftalan', 'Naftalan'),
        ('Naxçıvan', 'Naxçıvan'),
        ('Nefçala', 'Nefçala'),
        ('Oğuz', 'Oğuz'),
        ('Qax', 'Qax'),
        ('Qazax', 'Qazax'),
        ('Qəbələ', 'Qəbələ'),
        ('Qobustan', 'Qobustan'),
        ('Quba', 'Quba'),
        ('Qusar', 'Qusar'),
        ('Saatlı', 'Saatlı'),
        ('Sabirabad', 'Sabirabad'),
        ('Şabran', 'Şabran'),
        ('Şahbuz', 'Şahbuz'),
        ('Salyan', 'Salyan'),
        ('Şamaxı', 'Şamaxı'),
        ('Şamux', 'Şamux'),
        ('Şəki', 'Şəki'),
        ('Şəmkir', 'Şəmkir'),
        ('Şərur', 'Şərur'),
        ('Şirvan', 'Şirvan'),
        ('Siyəzən', 'Siyəzən'),
        ('Sumqayıt', 'Sumqayıt'),
        ('Tərtər', 'Tərtər'),
        ('Tovuz', 'Tovuz'),
        ('Ucar', 'Ucar'),
        ('Xaçmaz', 'Xaçmaz'),
        ('Xırdalan', 'Xırdalan'),
        ('Xızı', 'Xızı'),
        ('Xudat', 'Xudat'),
        ('Yardımlı', 'Yardımlı'),
        ('Yevlax', 'Yevlax'),
        ('Zaqatala', 'Zaqatala'),
        ('Zərdab', 'Zərdab'),
    )

    city = models.CharField(choices=SEH, max_length=100)
    price = IntegerRangeField(min_value=10, max_value=10000000, verbose_name='Qiymət (AZN)')
    text = models.TextField()
    posting_date = models.DateTimeField(auto_now_add=True)
    updating_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField()
    feature = NumpyImage(source=image)


# Create your models here.
