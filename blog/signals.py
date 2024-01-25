from django.db.models.signals import post_save
from django.dispatch import receiver
from blog.models import Comment, Blog
from video.models import Notification, PublicNotification
from accounts.models import User


@receiver(post_save, sender=Comment)
def create_reply_notification_signal(sender, instance, created, *args, **kwargs):
    """
    craete notification when user reply comment
    """
    if created:
        if instance.parent_id:
            if instance.parent.user != instance.user:
                message = f"کاربری به کامنت شما در مقاله {instance.blog.title} پاسخ داد"
                blog = instance.blog
                Notification.objects.create(
                    user=instance.parent.user, message=message, blog=blog
                )
        elif instance.user != instance.blog.author:
            message = f"کاربری زیر مقاله {instance.blog.title}شما کامنت گذاشت . "
            blog = instance.blog
            Notification.objects.create(
                user=instance.blog.author, message=message, blog=blog
            )


@receiver(post_save, sender=Blog)
def create_blog_notification_signal(sender, instance, created, *args, **kwargs):
    """
    craete notification when add new article
    """
    if created:
        message = f"مقاله {instance.title}  منتشرشد"
        blog = instance
        user = User.objects.all()
        public = PublicNotification.objects.create(message=message, blog=blog)
        public.user.set(user)
