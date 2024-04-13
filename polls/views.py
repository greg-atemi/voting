from django.db.models import F
from django.http import Http404
from django.urls import reverse
from . models import Candidate, Election
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect


def index(request):
    election_list = Election.objects.order_by("-pub_date")
    context = {"election_list": election_list}
    return render(request, "polls/index.html", context)

def detail(request, election_id):
    try:
        election = Election.objects.get(pk=election_id)
    except Election.DoesNotExist:
        raise Http404("Election does not exist")
    return render(request, "polls/detail.html", {"election": election})

def results(request, election_id):
    election = get_object_or_404(Election, pk=election_id)
    return render(request, "polls/results.html", {"election": election})

def vote(request, election_id):
    election = get_object_or_404(Election, pk=election_id)
    try:
        selected_candidate = election.candidate_set.get(pk=request.POST["candidate"])
    except (KeyError, Candidate.DoesNotExist):
        # Redisplay the election voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "election": election,
                "error_message": "You didn't select a candidate.",
            },
        )
    else:
        selected_candidate.votes = F("votes") + 1
        selected_candidate.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(election.id,)))