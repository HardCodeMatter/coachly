def all_objects(model):
    return model.objects.all()

def filter_objects(model, **kwargs):
    return model.objects.filter(**kwargs)

def get_objects(model, **kwargs):
    return model.objects.get(**kwargs)
