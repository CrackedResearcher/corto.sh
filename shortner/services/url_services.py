from ..models import Url
from django.db import transaction
from .url_generate import generate_url_slug
import os

def check_slug_exists(slug):
    url = Url.objects.filter(slug=slug)
    if url:
        return True
    else:
        return False

def get_url_data(user):
    url_data = Url.objects.filter(user=user)
    return url_data
    
def create_url(data, user):
    url = data.get("url")
    url_slug = generate_url_slug()
    app_host_url = os.getenv("APP_BASE_URL", "https://corto.sh/")
    short_url = app_host_url + url_slug

    max_retries = 5
    for _ in range(max_retries):
        url_slug = generate_url_slug()

        check_if_exists = check_slug_exists(url_slug)
        if not check_if_exists:
            url = Url.objects.create(user=user, original_url=url, short_url=short_url, slug=url_slug)
            return url, False

    
    return None, "Could not generate unique slug"

def get_url_details(id, user):
    url = Url.objects.filter(user=user, id=id).first()
    return url

def update_url_details(data, id, user):
    with transaction.atomic():
        qs = Url.objects.filter(user=user, id=id)
        if not qs.exists():
            return None

        qs.update(**data)
        return qs.first()
    

def delete_url_data(url_id, user):
    with transaction.atomic():
        qs = Url.objects.filter(user=user, id=url_id)

        if not qs.exists():
            return False, "URL doesn't exist"

        qs.delete()
        return True, "Deleted successfully"


def get_url_details_from_slug(slug):
    url = Url.objects.filter(slug=slug).first()
    if not url:
        return None
    else:
        return url
