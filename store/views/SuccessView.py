from django.views.generic import TemplateView

class SuccessView(TemplateView):
    template_name = "products/success.html"