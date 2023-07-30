from django.core.validators import FileExtensionValidator
from persiantools.jdatetime import JalaliDate
from django.utils.html import format_html
from django.urls import reverse
from django.db import models
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating

# local
from accounts.models import User
from blog.models import Blog


class Actors(models.Model):
    name= models.CharField('نام', max_length=30)
    slug = models.SlugField('اسلاگ', allow_unicode=True, blank=True, null=True, unique=True)
    created_at = models.DateTimeField('تاریخ آپلود دسته بندی', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('تاریخ به روز رسانی دسته بندی', auto_now=True, null=True)

    class Meta:
        verbose_name = 'بازیگر'
        verbose_name_plural = 'بازیگران'
        ordering = ['-updated_at']

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField('عنوان', max_length=30)
    slug = models.SlugField('اسلاگ', allow_unicode=True, blank=True, null=True, unique=True)
    created_at = models.DateTimeField('تاریخ آپلود دسته بندی', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('تاریخ به روز رسانی دسته بندی', auto_now=True, null=True)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی‌ها'
        ordering = ['-updated_at']

    def __str__(self):
        return self.title


class Video(models.Model):

    AGE_CHOICES = (
        ('20','+20' ),		
        ('14','+14' ),	
        ('10', '+10'),
    )

    title = models.CharField('عنوان', max_length=50)
    category = models.ManyToManyField(Category, related_name='videos', verbose_name='دسته بندی')
    actors = models.ManyToManyField(Actors, related_name='videos', verbose_name='بازیگران')
    description = models.TextField('توضیحات')
    meta_description = models.CharField('متادیسکریپشن', max_length=3000)
    image = models.ImageField('تصویر ویدئو', upload_to='images/thumbnails', null=True)
    video = models.FileField('ویدئو', upload_to='videos/', null=True, validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    trailer=models.FileField('تریلر', upload_to='videos/', null=True, validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    ratings = GenericRelation(Rating, related_query_name='stars')
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',related_query_name='hit_count_generic_relation')
    favorites = models.ManyToManyField(User, default=None, blank=None, related_name="favorites",
                                       verbose_name="مورد علاقه‌ها")
    age=models.CharField(max_length=10, choices=AGE_CHOICES, verbose_name="رده سنی",null=True, blank=True)
    time=models.CharField(max_length=30,verbose_name="مدت زمان",null=True, blank=True)
    created_at = models.DateTimeField('تاریخ آپلود ویدئو', auto_now_add=True)
    updated_at = models.DateTimeField('تاریخ به روز رسانی ویدئو', auto_now=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='videos',
                                verbose_name='سازنده محتوا')
    slug = models.SlugField('اسلاگ', unique=True, null=True, blank=True, allow_unicode=True)

    class Meta:
        verbose_name = 'ویدئو'
        verbose_name_plural = 'ویدئوها'
        ordering = ["-created_at"]

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="60px" height="50px">')
        else:
            return format_html('<h3 style="color: red">بدون تصویر</h3>')

    def __str__(self):
        return self.title

    show_image.short_description = 'تصویر'

    def get_jalali_date(self):
        return JalaliDate(self.created_at, locale=('fa')).strftime("%c")

    def get_absolute_url(self):
        return reverse('video:video_detail', kwargs={'slug': self.slug})



class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE , related_name='likes',verbose_name="کاربر")
    video=models.ForeignKey(Video,on_delete=models.CASCADE , related_name='likes',verbose_name="ویدئو")
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="زمان ایجاد")

    #Methods
    def __str__(self):
        return f"{self.user} , {self.video}"

    class Meta:
        verbose_name="پسند"
        verbose_name_plural="پسندها "
        ordering = ('created_at',)  


class Serial(models.Model):
    AGE_CHOICES = (
        ('20','+20' ),		
        ('14','+14' ),	
        ('10', '+10'),
    )
    video = models.ManyToManyField(Video , related_name='playes' , verbose_name='ویدیوها',null=True, blank=True,)
    name = models.CharField(max_length=120 , null=True , blank=True , verbose_name='نام سریال')
    image = models.ImageField(upload_to='serial' , verbose_name='تصویر جلد سریال')
    slug = models.SlugField('اسلاگ', unique=True, null=True, blank=True, allow_unicode=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',related_query_name='hit_count_generic_relation')
    created_at = models.DateTimeField('تاریخ آپلود سریال ',auto_now_add=True )
    age=models.CharField(max_length=10, choices=AGE_CHOICES, verbose_name="رده سنی",null=True, blank=True)
    year=models.IntegerField('سال ساخت سریال',null=True, blank=True)

    def __str__(self) :
        return self.name

    def get_jalali_date(self):
        return JalaliDate(self.created_at, locale=('fa')).strftime("%c")
    
    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="60px" height="50px">')
        else:
            return format_html('<h3 style="color: red">بدون تصویر</h3>')

    show_image.short_description = 'تصویر'
    
    def get_absolute_url(self):
        return reverse('video:serial_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'سریال'
        verbose_name_plural = 'سریال ها'
        ordering = ["-created_at"]

class Season(models.Model):
    SEASON_CHOICES = (
        ('فصل1','فصل1' ),		
        ('فصل2','فصل2' ),	
        ('فصل3', 'فصل3'),
        ('فصل4', 'فصل4'),
    )
    name=models.CharField(max_length=10, choices=SEASON_CHOICES, verbose_name="شماره فصل",null=True, blank=True)
    season=models.ForeignKey(Serial,on_delete=models.CASCADE , related_name='seasons',verbose_name="سریال",null=True,blank=True)
    subject=models.CharField(max_length=10, verbose_name="موضوع فصل",null=True, blank=True)
    video = models.ManyToManyField(Video , related_name='videos' , verbose_name='ویدیوها')
    image = models.ImageField(upload_to='serial/season' , verbose_name='تصویر جلد فصل')
    slug = models.SlugField('اسلاگ', unique=True, null=True, blank=True, allow_unicode=True)
    created_at = models.DateTimeField('تاریخ آپلود فصل ',auto_now_add=True )

    def __str__(self) :
        return self.name

    def get_jalali_date(self):
        return JalaliDate(self.created_at, locale=('fa')).strftime("%c")
    
    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="60px" height="50px">')
        else:
            return format_html('<h3 style="color: red">بدون تصویر</h3>')

    show_image.short_description = 'تصویر'
    
    def get_absolute_url(self):
        return reverse('video:season_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'فصل'
        verbose_name_plural = 'فصل ها'
        ordering = ["-created_at"]



class Notification(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True, related_name='notifs',verbose_name="کاربر")
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="زمان ایجاد")
    message = models.TextField()
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE, null=True, blank=True, related_name='notifs',verbose_name="مقاله")

    class Meta:
        verbose_name="خبر"
        verbose_name_plural="اخبار"
        ordering = ('-created_at',)

    def get_jalali_date(self):
        return JalaliDate(self.created_at, locale=('fa')).strftime("%c")

    def __str__(self):
        return f"{self.user} , {self.message[:10]}"



class PublicNotification(models.Model):
    user=models.ManyToManyField(User, related_name='public',verbose_name="کاربر")
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="زمان ایجاد")
    message = models.TextField()
    video=models.ForeignKey(Video,on_delete=models.CASCADE, null=True, blank=True, related_name='public',verbose_name="ویدئو")
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE, null=True, blank=True, related_name='public',verbose_name="مقاله")
    serial=models.ForeignKey(Serial,on_delete=models.CASCADE, null=True, blank=True, related_name='public',verbose_name="سریال")
    season=models.ForeignKey(Season,on_delete=models.CASCADE, null=True, blank=True, related_name='public',verbose_name="فصل")

    class Meta:
        verbose_name=" خبر عمومی"
        verbose_name_plural="اخبار عمومی"
        ordering = ('-created_at',)

    def get_jalali_date(self):
        return JalaliDate(self.created_at, locale=('fa')).strftime("%c")

    def __str__(self):
        return f"{self.user} , {self.message[:10]}"