from django.shortcuts import render, redirect
from dashapp.models import Team
from django.views.generic import View
from django.views.generic import ListView, DetailView
from dashapp.models import Team, Members, FemalePresenter, MalePresenter
# Create your views here.
def voting(request):
    return render(request,"voteapp/voting.html")

def votes(request):
    all_teams = Team.objects.all()
    #pdgroup = get_object_or_404(self)
    try:
        select_pdgroup = Team.objects.get(pk=request.POST['team'])
        select_pdgroup.vote_count +=1
    except (KeyError, Team.DoesNotExist):
        return render(request, 'voteapp/voteteams.html', { 'all_teams':all_teams }, { 'error_message':"You did not select a valid pd group", })
    else:
        select_pdgroup.save()
        print(select_pdgroup)  
        return redirect('voteapp:males')  
    return render(request, 'voteapp/voteteams.html', { 'all_teams':all_teams })

def males(request):
    all_males = MalePresenter.objects.all()
    try:
        select_malepresenter = MalePresenter.objects.get(pk=request.POST['male'])
        select_malepresenter.vote_count +=1
    except (KeyError, MalePresenter.DoesNotExist):
        return render(request,'voteapp/malepresenter.html', {'all_males':all_males}, { 'error_message':"You did not select a valid male presenter"})    
    else:
        select_malepresenter.save()
        print(select_malepresenter)
        return redirect('voteapp:females') 
    return render(request,'voteapp/malepresenter.html', {'all_males':all_males}, { 'error_message':"You did not select a valid male presenter"})    

def females(request):
    all_females = FemalePresenter.objects.all()
    
    try:
        select_femalepresenter = FemalePresenter.objects.get(pk=request.POST['female'])
        select_femalepresenter.vote_count +=1
    except (KeyError, MalePresenter.DoesNotExist):
        return render(request,'voteapp/femalepresenter.html', {'all_females':all_females}, { 'error_message':"You did not select a valid male presenter"})    
    else:
        select_femalepresenter.save()
        print(select_femalepresenter)
    return render(request,'voteapp/femalepresenter.html', {'all_females':all_females}, { 'error_message':"You did not select a valid male presenter"})    

