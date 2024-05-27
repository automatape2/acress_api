from .models import Pubinei

def get_pubinei(distrito):
    pubinei = Pubinei.objects.filter(key=distrito).first()
    return pubinei

def insert_pubinei(pubinei):
    pubinei.save()
    return pubinei
