from django.shortcuts import render, redirect
from django.views.generic import ListView

from feedback.forms import FeedbackForm
from feedback.models import Feedback


# Create your views here.
def success_feedback(request):
    return render(request, 'feedback/success_page.html')


def create_feedback(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        form.save()
        return redirect('success-feedback')

    context = {
        'form': form
    }
    return render(request, 'feedback/create.html', context)


class FeedbackListView(ListView):
    model = Feedback
    queryset = Feedback.objects.order_by('-created_at').filter(is_confirmed=True)
    template_name = 'feedback/list.html'
    paginate_by = 10
