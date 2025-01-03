from django.shortcuts import render ,redirect , get_object_or_404
from django.http import HttpResponseRedirect 
from post.models import Tag,Follow,Post,Stream,Likes
from post.forms import NewPostForm
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required
from userauths.models import Profile
from comment.models import Comment 
from comment.forms import CommentForm


def index(request):
    user = request.user    
    posts = Stream.objects.filter(user=user)
    group_ids = []
    for post in posts:
        group_ids.append(post.post_id)
    post_items = Post.objects.filter(id__in=group_ids).order_by('-posted')    
    context = {
        'post_items': post_items
    }
    
    return render(request , 'index.html',context)

def NewPost(request):
    user = request.user.id
    tags_objs = []
    
    if request.method == 'POST':
        form=NewPostForm(request.POST , request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get('picture')
            caption = form.cleaned_data.get('caption') 
            tag_form = form.cleaned_data.get('tag') 
            tags_list = list(tag_form.split(','))
            for tag in tags_list:
                t, created = Tag.objects.get_or_create(title=tag)
                tags_objs.append(t)
            
            p, created = Post.objects.get_or_create(picture=picture, caption=caption, user_id=user)
            p.tag.set(tags_objs)
            p.save()
            return redirect ('index')
    else : 
        form=NewPostForm()
        context={
            'form':form
        }  
    return render(request, 'newpost.html',context)
        
def PostDetail(request , post_id):
    post = get_object_or_404(Post ,id.post_id)
    #comment 
    
    comments=Comment.objects.filter(post=post).order_by("-date")
    
    #commentform
    if request.method == "POST":
        form=CommentForm(request.POST ,request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            
            return HttpResponseRedirect(reverse("post-details",args=[post_id]))
    else : 
        form=CommentForm()
        context={
            'form':form,
            'comments': comments , 
            'post' : post
        }  
        
    return render (request , 'post_details.html')

def Tags(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags=tag).order_by('-posted')

    context = {
        'posts': posts,
        'tag': tag

    }
    return render(request, 'tags.html', context)


def like(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    current_likes = post.likes
    liked=Likes.objects.filter(user=user , post=post).count()
    if not liked:
        liked=Likes.objects.create(user=user , post=post)
        current_likes =current_likes+1
    else:
        liked=Likes.objects.filter(user=user , post=post).delete()
        current_likes = current_likes -1
    
    post.likes=current_likes
    post.save()
    return HttpResponseRedirect(reverse('post-details',args=[post_id]))
    
def favourite(request,post_id):
    user = request.user
    post = Post.objectq.get(id=post_id)
    profile=Profile.objects.get(user=user)
    if profile.favourite.filter(id=post_id).exists() :
        profile.favourite.remove(post)
    else:
        profile.favourite.add(post)
    return HttpResponseRedirect(reverse('post_details',args=[post_id]))