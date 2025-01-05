from    modeltranslation.translator import register, TranslationOptions
from .models import ServiceModel, PartnerModel, FunctionsModel, Customer_Opinion


@register(ServiceModel)
class ServiceOption(TranslationOptions):
    fields = ('title', 'description', 'little_desc')

@register(PartnerModel)
class ServiceOption(TranslationOptions):
    fields = ('position', 'opinion')


@register(FunctionsModel)
class ServiceOption(TranslationOptions):
    fields = ('name', 'description')


@register(Customer_Opinion)
class ServiceOption(TranslationOptions):
    fields = ('opinion', 'full_name')