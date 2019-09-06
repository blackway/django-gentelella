import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Language

logger = logging.getLogger(__name__)

# django signals 설정
@receiver(post_save, sender=Language)
def language_post_save( sender, **kwargs ):
    logger.debug('@@@@@@@@@@@@@@ language_post_save ')
    # logger.debug('@@@@@@@@@@@@@@ kwargs ' % kwargs)
    instance = kwargs['instance']
    # location = kwargs['instance'].location
    logger.debug('@@@@@@@@@@@@@@ instance %s' % instance)
    # location.num_pizzazip += 1
    # location.save( )

# post_save.connect(language_post_save, sender=Language)
