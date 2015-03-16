from django.shortcuts import render_to_response

# Create your views here.
def EntryPicks(request):
	return render_to_response('brackets/entry.html')