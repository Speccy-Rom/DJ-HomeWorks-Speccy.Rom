from django.conf import settings
from os import listdir, stat
from os.path import isfile, join


def get_only_files():
    only_files = [f for f in listdir(settings.FILES_PATH) if isfile(join(settings.FILES_PATH, f))]

    return only_files


def get_file_path(filename):
    return join(settings.FILES_PATH, filename)