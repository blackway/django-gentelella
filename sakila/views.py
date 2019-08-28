# -*- coding: utf-8 -*-
import json
import logging

from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
# from pip._vendor.requests import Response
from django.views.generic import ListView
from django.views.generic .edit import CreateView
from django.views import View

from sakila.forms import CustomerForm
from .models import Customer

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


class CustomerListView(ListView):
    """
    클래스 뷰
    """
    model = Customer
    template_name = 'sakila/tables_dynamic_customer.html'
    context_object_name = 'list'


class CustomerAjaxView(View):
    """
    Ajax 처리
    """

    form_class = CustomerForm
    initial = {'key': 'value'}

    def post(self, request):
        if request.is_ajax():
            # data = {"lat":20.586, "lon":-89.530}
            # print(request.POST.get('value'))
            logger.debug(' class name : %s ' % 'CustomerAjaxView')
            logger.debug(' function name : %s ' % 'post')
            # film_id = request.POST['film_id']
            # description = request.POST['description']
            # special_features = request.POST['special_features']

            form = self.form_class(request.POST)

            if form.is_valid():
                data = {
                    "msg": "성공",
                }
                form.save()
                return JsonResponse(data, json_dumps_params={'ensure_ascii': False})

            logger.debug(' error msg : %s ' % form.errors)
            # film = get_object_or_404(Film, pk=film_id)
            # form = CustomerForm(request.P)
            # film.description = description
            # film.special_features = special_features
            # film.save()
            # tmpJson = serializers.serialize("json",film)
            # tmpObj = json.loads(tmpJson)
            data = {
                "msg": "실패",
                "errors": str(form.errors) # str() 자동형 변환 하지 못하게 함 그러면 html 로 생성됨.
                # "errors": form.errors
            }
            return JsonResponse(data,  json_dumps_params={'ensure_ascii': False})

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, 'landing.html', {'form': form})


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


# class CustomerAjaxCreateView(AjaxableResponseMixin, CreateView):
class CustomerAjaxCreateView(CreateView):
    """
    Ajax 처리 Create
    """
    model = Customer
    # fields = ['first_name']
    # initial={'date_of_death':'05/01/2018',}
    # initial = {'key': 'value'}
    # # form_class = Customer
    # #
    def get(self, request):
        form = CustomerForm()
        # form = self.form_class()
        # form = self.form_class(initial=self.initial)
        data = {
            'form_as_table': form.as_table(),
        }
        return JsonResponse(data,  json_dumps_params={'ensure_ascii': False})


    def post(self, request):
        self.form_class = CustomerForm
        # initial = {'key': 'value'}
        if request.is_ajax():
            # data = {"lat":20.586, "lon":-89.530}
            # print(request.POST.get('value'))
            logger.debug(' class name : %s ' % 'CustomerAjaxCreateView')
            logger.debug(' function name : %s ' % 'post')
            # film_id = request.POST['film_id']
            # description = request.POST['description']
            # special_features = request.POST['special_features']

            form = self.form_class(request.POST)

            if form.is_valid():
                data = {
                    "msg": "성공",
                }
                form.save()
                return JsonResponse(data, json_dumps_params={'ensure_ascii': False})

            logger.debug(' error msg : %s ' % form.errors)
            # film = get_object_or_404(Film, pk=film_id)
            # form = CustomerForm(request.P)
            # film.description = description
            # film.special_features = special_features
            # film.save()
            # tmpJson = serializers.serialize("json",film)
            # tmpObj = json.loads(tmpJson)
            data = {
                "msg": "실패",
                "errors": str(form.errors) # str() 자동형 변환 하지 못하게 함 그러면 html 로 생성됨.
                # "errors": form.errors
            }
            return JsonResponse(data,  json_dumps_params={'ensure_ascii': False})
