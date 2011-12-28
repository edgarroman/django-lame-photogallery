from django.conf import settings

def branding_variables(request):
    brand_dict = {
        'brand_copyright': settings.BRAND_COPYRIGHT,
        'brand_title' : settings.BRAND_SITE_TITLE,
        'brand_logo' : settings.BRAND_LOGO,
        'brand_ga_code' : settings.BRAND_GA_CODE,
    }
    return brand_dict

