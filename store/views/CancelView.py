from django.views.generic import TemplateView

class CancelView(TemplateView):
    template_name = "products/cancel.html"