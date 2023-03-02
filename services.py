from django.core.exceptions import ObjectDoesNotExist


def all_objects(model):
    return model.objects.all()

def filter_objects(model, **kwargs):
    return model.objects.filter(**kwargs)

def get_objects(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except ObjectDoesNotExist:
        return None
