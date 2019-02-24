from django.db import models

from model_utils import Choices


class Students(models.Model):
    name = models.CharField(max_length=50)
    NIS = models.CharField(max_length=50)
    GRADE = Choices(
        (1, 'sepuluh', 'X'),
        (2, 'sebelas', 'XI'),
        (3, 'duabelas', 'XII')
    )
    ACADEMIC_FIELD = Choices(
        (1, 'RPL', 'Rekayasa Perangkat Lunak'),
        (2, 'TKJ', 'Teknik Komputer Jaringan'),
        (3, 'AKT', 'Akuntansi'),
        (4, 'AP', 'Administrasi Perkantoran'),
        (5, 'TN', 'Tata Niaga'),
    )
    academic_field = models.PositiveSmallIntegerField(choices=ACADEMIC_FIELD)
    grade = models.PositiveSmallIntegerField(choices=GRADE)
    GENDER = Choices(
        (1, 'male', 'Male'),
        (2, 'female', 'Female')
    )
    gender = models.PositiveSmallIntegerField(choices=GENDER)
    email = models.EmailField('email address', unique=True, max_length=254)

    def __str__(self):
        return self.name