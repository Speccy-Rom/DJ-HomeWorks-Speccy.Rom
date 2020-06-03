import datetime
from os import stat
from django.shortcuts import render
from django.http import HttpResponseNotFound
from app.get_info import get_only_files, get_file_path


def file_list(request, date=None):
    template_name = 'index.html'

    files = []
    only_files = get_only_files()

    for file in only_files:
        file_info = stat(get_file_path(file))
        ctime = datetime.datetime.fromtimestamp(file_info.st_ctime)
        mtime = datetime.datetime.fromtimestamp(file_info.st_mtime)

        files.append({
            'name': file,
            'ctime': ctime,
            'mtime': mtime
        }) if (date == ctime.date() or date == mtime.date()) or (not date) else None

    context = {
        'files': files,
        'date': date
    }

    return render(request, template_name, context)


def file_content(request, name):

    if name not in get_only_files():
        return HttpResponseNotFound()

    with open(get_file_path(name)) as file_open:
        content = ''
        for line in file_open.read():
            content += line

    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': content}
    )