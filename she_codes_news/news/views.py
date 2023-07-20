from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm


class IndexView(generic.ListView):
        template_name = 'news/index.html'
        context_object_name = "all_stories"
        
        def get_queryset(self):
            '''Return all news stories ordered by pub_date in descending order.'''
            return NewsStory.objects.order_by('-pub_date')
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['latest_stories'] = NewsStory.objects.order_by('-pub_date')[:4]  # Fetch the 4 latest stories based on pub_date
            return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):  
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
   

    

   