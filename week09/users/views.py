from django.shortcuts import render, redirect, get_object_or_404
from .models import User
import pdb


def follow_toggle(request, id):
    ## pass 아무것도 안하는것
    user = request.user
    if user.is_anonymous:
        return redirect('account_login')
        
    followed_user = get_object_or_404(User, pk=id)
    
    is_follower = user in followed_user.followers.all()
    
    if is_follower:
        user.following.remove(followed_user)
        # user.followings.remove(followed_user)
        # followed_user.followers.remove(user)
    else:
        user.following.add(followed_user)
        # user.followings.add(followed_user)
        # pdb.set_trace()
        # followed_user.followers.add(user)
    
    return redirect('home')