from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from unit.models import Unit


@receiver(pre_save, sender=Unit)
def create_unit_fields(sender, instance, **kwargs):

    instance.full_name = f'{instance.type.type_full} {instance.city} {instance.zip_code}, {instance.address}'
    text = f'{instance.type.type_short} {instance.city} {instance.address} {instance.id}'

    if instance.slug != text:
        instance.slug = slugify(text, )