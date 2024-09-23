from django.shortcuts import render, redirect, get_object_or_404
from .forms import CandidateCreationForm, CandidateUpdateForm
from .models import Candidate

# Create your views here.
def home(request):
    return render(request,"Core/index.html")


def create_candidate(request):
    if request.method == 'POST':
        form = CandidateCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Create the user
            # Create the candidate record
            Candidate.objects.create(
                post=form.cleaned_data['post'],
                manifesto=form.cleaned_data['manifesto'],
                background_info=form.cleaned_data['background_info'],
                user=user  # Assuming there’s a ForeignKey to CustomUser in Candidate model
            )
            return redirect('/')  # Redirect to a success page
    else:
        form = CandidateCreationForm()
    
    return render(request, 'Candidates/create_candidate.html', {'form': form})

def update_candidate(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)
    user = candidate.user  # Assuming there’s a ForeignKey to CustomUser in Candidate model
    
    if request.method == 'POST':
        form = CandidateUpdateForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()  # Update the user
            # Update the candidate record
            candidate.post = form.cleaned_data['post']
            candidate.manifesto = form.cleaned_data['manifesto']
            candidate.background_info = form.cleaned_data['background_info']
            candidate.save()
            return redirect('/')  # Redirect to a success page
    else:
        form = CandidateUpdateForm(instance=user)

    return render(request, 'update_candidate.html', {'form': form, 'candidate': candidate})
