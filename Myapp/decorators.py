from django.contrib import messages

from django.shortcuts import redirect



def SignIn_required(fn):
    
    def wrapper(request,*args, **kwargs):
        
        if not request.user.is_authenticated:
            
            messages.error(request,"Invalid Session")
            
            return redirect("sign-in")
        
        else:
            
            return fn(request,*args,**kwargs)
        
    return wrapper