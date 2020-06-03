from django.shortcuts import render
import os
import csv

def inflation_view(request):
    template_name = 'inflation.html'
    p = os.path.dirname(os.path.dirname(__file__))
    file = os.path.abspath(os.path.join(p, 'inflation_russia.csv'))
    list_inf = []
    with open(file, newline='', encoding='utf8') as f:
        reader = csv.reader(f)
        print(reader)
        for line in reader:
            for i in line:
                list = i.split(';')
                list_inf.append(list)
    # чтение csv-файла и заполнение контекста
    list1 = list_inf.pop(0)

    context = {'list': list_inf, 'list1':list1}

    return render(request, template_name,
                  context)