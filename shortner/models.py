from django.contrib.auth.models import User
from django.db import models
import pendulum

class Url(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField(verbose_name="original url", max_length=2048)
    short_url = models.URLField(verbose_name="shortened url", max_length=25, blank=True, null=True, unique=True)
    slug = models.CharField(max_length=8, blank=True, null=True, db_index=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        created_human = pendulum.instance(self.created_at).diff_for_humans()
        return f"{self.slug} - {created_human}"


class AnalyticData(models.Model):
    url = models.ForeignKey(Url, on_delete=models.CASCADE, related_name="analytics_data")
    total_visits = models.PositiveBigIntegerField(verbose_name="times url visited", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.total_visits} visit - {self.url.short_url}"