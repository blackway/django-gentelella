# -*- coding: utf-8 -*-
import json
import logging

from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from pip._vendor.requests import Response

from .models import Film

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
        list_cnt = Film.objects.count()
        logger.debug(' function name list_cnt : %s ' % list_cnt)
        context = {'list': list}

    template = loader.get_template('sakila/' + load_template)
    return HttpResponse(template.render(context, request))


# 여기서에서 @csrf_exempt 는 csrf 보안을 사용 하기 않겠다는 의미 입니다.  참조사이트 [ django csrf 문서 ]
# @csrf_exempt
def film_modify(request):
    logger.debug(' function name : %s ' % 'film_modify')
    film_id = request.POST['film_id']
    description = request.POST['description']
    special_features = request.POST['special_features']

    film = get_object_or_404(Film, pk=film_id)
    film.description = description
    film.special_features = special_features
    film.save()
    # tmpJson = serializers.serialize("json",film)
    # tmpObj = json.loads(tmpJson)
    context = {
        "msg": "성공",
    }
    # return HttpResponse(context, content_type="application/json; charset=utf-8")
    # return HttpResponse(json.dumps(context), content_type="application/json; charset=utf-8")
    # return JsonResponse({
    #     'message': '안녕 파이썬 장고',
    #     'items': ['파이썬', '장고', 'AWS', 'Azure'],
    # }, json_dumps_params={'ensure_ascii': True})
    # 한글 잘 보임
    return HttpResponse(json.dumps(context, ensure_ascii=False), content_type="application/json")
    # return JsonResponse(json.dumps(context, ensure_ascii=False), safe=False)
    # return Response(context, content_type='application/json; charset=utf-8')



def list_staff(request):
    print('@@@@@@@@@@@@@@@@')
    load_template = request.path.split('/')[-1]
    logger.debug(' function name load_template : %s ' % load_template)
    context = {}
    # list = Staff.objects.all()
    # list_cnt = Staff.objects.count()
    # logger.debug(' function name list_cnt : %s ' % list_cnt)
    # context = {'list': list}
    template = loader.get_template('sakila/tables_dynamic.html')
    return HttpResponse(template.render(context, request))





