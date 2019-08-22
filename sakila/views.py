import logging

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from sakila.models import Staff, Film

logger = logging.getLogger('default')
# logger = logging.getLogger(__name__)
# logging.disable(logging.NOTSET)
# logger.setLevel(logging.DEBUG)


def index(request):
    print('@@@@@@@@@@@@@@@@')
    context = {}
    template = loader.get_template('sakila/index.html')
    return HttpResponse(template.render(context, request))


def gentella_html(request):
    print('@@@@@@@@@@@@@@@@')
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    logger.debug(' function name gentella_html : %s ' % load_template)
    if load_template == 'tables_dynamic.html':
        list = Film.objects.all()
        list_cnt = Staff.objects.count()
        logger.debug(' function name list_cnt : %s ' % list_cnt)
        context = {'list': list}

    template = loader.get_template('sakila/' + load_template)
    return HttpResponse(template.render(context, request))


def list_staff(request):
    print('@@@@@@@@@@@@@@@@')
    load_template = request.path.split('/')[-1]
    logger.debug(' function name load_template : %s ' % load_template)
    list = Staff.objects.all()
    list_cnt = Staff.objects.count()
    logger.debug(' function name list_cnt : %s ' % list_cnt)
    context = {'list': list}
    template = loader.get_template('sakila/tables_dynamic.html')
    return HttpResponse(template.render(context, request))