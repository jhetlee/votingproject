from django.shortcuts import render, redirect, get_object_or_404
from dashapp.models import Team, Members, FemalePresenter, MalePresenter
from dashapp.forms import TeamForm, MemberForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from dashapp.forms import UserForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View

# Create your views here.

class TeamList(ListView):
    template_name = 'dashapp/teams.html'
    context_object_name = 'all_teams'
    def get_queryset(self):
        return Team.objects.all()

class FemaleList(ListView):
    template_name = 'dashapp/female_presenters.html'
    context_object_name = 'all_females'
    def get_queryset(self):
        return FemalePresenter.objects.all()

class MaleList(ListView):
    template_name = 'dashapp/male_presenter.html'
    context_object_name = 'all_males'
    def get_queryset(self):
        return MalePresenter.objects.all()

class ToptemsDetails(ListView):
    template_name = 'dashapp/top_teams.html'
    context_object_name = 'top_teams'
    def get_queryset(self):
        return Team.objects.order_by('-vote_count')[:5]                 #orderby votecounts top 5

class TopFemales(ListView):
    template_name = 'dashapp/top_females.html'
    context_object_name = 'top_females'
    def get_queryset(self):
        return FemalePresenter.objects.order_by('-vote_count')[:5]                 #orderby votecounts top 5
    
class TopMales(ListView):
    template_name = 'dashapp/top_males.html'
    context_object_name = 'top_males'
    def get_queryset(self):
        return MalePresenter.objects.order_by('-vote_count')[:5]                 #orderby votecounts top 5



class TeamDetails(DetailView):
    model = Team
    template_name = 'dashapp/team_detail.html'

class CreateTeam(CreateView):
    model = Team
    fields = ['team_name', 'team_project', 'bio']


class AddFemale(CreateView):
    model = FemalePresenter
    fields = ['team', 'fName', 'lName']


class AddMale(CreateView):
    model = MalePresenter
    fields = ['team', 'fName', 'lName']


class UserFormView(View):
    form_class=UserForm
    template_name = 'dashapp/voter_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        context = {
            'form':form
        }
        return render(request, self.template_name, context)
    
    #process form data
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            #cleaned normalize data
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user.set_password(password)
            user.save()
        #returns User objects if credentials are correct
        user = authenticate(username=username, password=password)
        context = {
        'form': form,
        'success_message':'user.username added'
        }
        if user is not None:

            if user.is_active:
                login(request, user)
                return redirect('voteapp:voting') 
        
        return render(request, self.template_name,context) 


def add_member(request, team_id):
    form = MemberForm(request.POST or None)
    team = get_object_or_404(Team, pk=team_id)

    if form.is_valid():
        context = {
        'team': team,
        'form': form,
        }
        members = form.save(commit=False)
        members.team = team
        members.save()
        return render(request, 'dashapp/team_detail.html', context)
        
    context = {
        'team': team,
        'form': form,
    }

    return render(request, 'dashapp/members_form.html', context)