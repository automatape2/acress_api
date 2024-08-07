from django.core.management.base import BaseCommand
from tqdm import tqdm
from app.pubinei.models import Pubinei, Poblacion
import pandas
from app.helpers.services import convert_to_slug
import json
from app.NBI.models import NBI
import os

class Command(BaseCommand):
    pass