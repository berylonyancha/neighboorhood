from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import UserProfile,Post,Neighborhood,Company,Comment
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm,CompanyForm,PostForm,CommentForm
# Create your views here.
@login_required
def index(request):
    current_user = request.user
    try:
        profile = UserProfile.objects.get(user = current_user)
    except:
        return redirect('edit_profile',username = current_user.username)

    try:
        posts = Post.objects.filter(neighborhood = profile.neighborhood)
    except:
        posts = None

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.neighborhood = profile.neighborhood
            post.type = request.POST['type']
            post.save()
        return redirect('index')
    else:
        form = PostForm()
    return render(request,'index.html',{"posts":posts,"profile":profile,"form":form})
@login_required
def edit_profile(request,username):
    current_user = request.user
    if request.method == 'POST':
        try:
            profile = UserProfile.objects.get(user=current_user)
            form = UserProfileForm(request.POST,instance=profile)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = current_user
                profile.save()
            return redirect('index')
        except:
            form = UserProfileForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = current_user
                profile.save()
            return redirect('index')
    else:
        if UserProfile.objects.filter(user=current_user):
            profile = UserProfile.objects.get(user=current_user)
            form = UserProfileForm(instance=profile)
        else:
            form = UserProfileForm()
    return render(request,'edit_profile.html',{"form":form})


@login_required
def companies(request):
    current_user = request.user
    neighborhood = UserProfile.objects.get(user = current_user).neighborhood
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = current_user
            company.neighborhood = neighborhood
            company.save()
            return redirect('companies')
    else:
        form = CompanyForm()

    try:
        companies = Company.objects.filter(neighborhood = neighborhood)
    except:
        companies = None

    return render(request,'companies.html',{"companies":companies,"form":form})

