from django.utils.translation import gettext_lazy as _
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm, forms
from .models import Customer
import logging


logger = logging.getLogger('default')


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        # fields = ['__all__']
        # fields = ['first_name', 'last_name']
        # 아래 항목은 cleaned_data 를 하기 위함, pk 는 안하고, self.data.get('pk키') 로 받음.
        # fields = ('first_name', 'last_name')
        fields = '__all__'
        exclude = ('address_id', 'customer_id', 'create_date', 'active', 'last_update', 'store_id')
        error_messages = {
            'last_name': {
                'required': _("필수 입력 입니다."),
                'max_length': _("입력 값이 너무 길어요"),
                # 'max_length': _("This writer's name is too long."),
            },
        }
        # def clean_last_name(self):
        #     'username 필드값의좌/우 공백을 제거하고, 최소 3글자 이상 입력되었는지 체크'
        #     last_name = self.cleaned_data.get('last_name', '').strip()
        #     if last_name:
        #         if len(last_name) < 3:
        #             raise forms.ValidationError('3글자 이상 입력해주세요.')
        #             # 이 리턴값으로 self.cleaned_data['username'] 값이 변경됩니다.
        #             # 좌/우 공백이 제거된 (strip) username으로 변경됩니다.
        #     return last_name
        #
        # def clean(self):
        #     cleaned_data = super().clean()
        #     # if self.check_exist(cleaned_data['server'], cleaned_data['last_name']):
        #     if not cleaned_data('last_name'):
        #         # clean내 ValidationError는 non_field_errors 로서 노출
        #         # raise forms.ValidationError('서버에 이미 등록된 username입니다.')
        #         raise forms.ValidationError({'last_name': _('서버에 이미 등록된 username입니다.')})
        #     return cleaned_data
        #
        # def check_exist(self, server, last_name):
        #     return Customer.objects.filter(server=server, last_name=last_name).exists()



        # fields = '__all__'
        # error_messages = {
        #     # 'some_integer_field': {
        #     #     'invalid': 'some custom invalid message',
        #     # },
        #     'last_name': {
        #         'invalid': '폼에서 에러 재정의',
        #     },
        # }
        # error_messages = {
        #     NON_FIELD_ERRORS: {
        #         'last_name': "%(model_name)s's %(field_labels)s are not unique.",
        #     }
        #     # 'last_name': {
        #     #     'max_length': _("This writer's name is too long."),
        #     # },
        # }

    # def clean(self):
    #     data = self.cleaned_data
    #     print('data : ', data)
    #     if not data.get('last_name'):
    #     # if self.last_name is not None:
    #         raise forms.ValidationError({'last_name': _('Draft entries may not have a publication date.')})
    #     # if data['num_values'] != data['num_average'] * 3:
    #     #     raise forms.ValidationError('values must be three times average')
    #

    def save(self, commit=True):
        """
        저장
        ModelForm 을 사용시에는 save 함수를 다시 구형 해줘야함.
        그렇지 모델에 있는 항목 전부를 request 에서 받으려함. 그러다 없으면 null 로 쿼리를 수행함.
        :param commit:
        :return:
        """
        logger.debug('forms save first_name : %s ' % self.cleaned_data.get('first_name'))
        logger.debug('forms save last_name : %s ' % self.cleaned_data.get('last_name'))
        customer_id = self.data.get('customer_id')
        logger.debug('forms save customer_id : %s ' % customer_id)

        update_cnt = Customer.objects.filter(pk=customer_id).update(
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name')
        )
        logger.debug('forms save update_cnt : %s ' % update_cnt)
        if not update_cnt:
            obj, created = Customer.objects.get_or_create(
                first_name=self.cleaned_data.get('first_name'),
                last_name=self.cleaned_data.get('last_name'),
                defaults={'customer_id': customer_id})
            logger.debug('forms save get_or_create : %s ' % created)
            return obj

        # logger.debug('save customer_id : %s ' % self.cleaned_data.get('customer_id'))
        # update_cnt = Customer.objects.filter(pk=customer_id).update(
        #     first_name=self.cleaned_data.get('first_name'),
        #     last_name=self.cleaned_data.get('last_name')
        # )
        # return update_cnt
        # customer_author, created = Customer.objects.update_or_create(
        #     first_name=self.cleaned_data.get('first_name'),
        #     last_name=self.cleaned_data.get('last_name'),
        #     defaults={'customer_id': customer_id})
        # return customer_author
        # user_author, created = Customer.objects.update_or_create(first_name=self.first_name,
        # author=self.author,
        # defaults={'is_follow': self.cleaned_data.get('is_follow'), 'review': self.cleaned_data.get('review')} )
        #rest of your logic
        # return update_cnt