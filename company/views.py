# Create your views here.
from django.shortcuts import render
from django.views.generic import DetailView

from company.models import AllConstruct, Construct


def test(request):
    if request.method == 'GET':
        all_post = AllConstruct.objects.all().filter(type_construct=request.current_page)
        return render(request, 'construct_types.html', {'type_construct': all_post})


class ConstructDetailView(DetailView):
    model = Construct
    context_object_name = 'construct'
    template_name = 'construct_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ConstructDetailView, self).get_context_data(**kwargs)
        context['back_url'] = self.request.current_page.application_urls
        context['category_detail'] = self.object
        return context

    def post(self, request, pk):
        return self.get(request, pk)
