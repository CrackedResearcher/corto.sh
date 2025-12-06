from ..models import Url

def get_url_data(user):
    url_data = Url.objects.filter(user=user)
    print("url data in get url data => ", url_data)
    return url_data
    
def create_url(data, user):
    url = data.get("url")
    exists = Url.objects.filter(user=user, original_url=data.get("url"))
    if exists:
        return False, "Url already exists"
    else:
        print("rannnnnnn")
        url = Url.objects.create(user=user, original_url=url, short_url="https://google.com/11")
        print("url")
        return url, False

def get_url_details(id, user):
    url = Url.objects.filter(user=user, id=id).first()
    return url

def update_url_details(data, id, user):
    qs = Url.objects.filter(user=user, id=id)
    if not qs.exists():
        return None

    qs.update(**data)
    return qs.first()
    

def delete_url_data(id, user):
    qs = Url.objects.filter(user=user, id=id)
    count, _ = qs.delete()

    if count > 0:
        return True, "Deleted Successfully"
    else:
        return False, "Url doesnt exist"
