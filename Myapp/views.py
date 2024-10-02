from django.shortcuts import render,redirect

from django.views.generic import View

from Myapp.forms import AlbumForm,SongsForm,RegistrationForm,SignInForm

from Myapp.models import Album,Songs

from django.contrib.auth import authenticate,login,logout

from django.utils.decorators import method_decorator

from Myapp.decorators import SignIn_required

from django.contrib import messages

# Create your views here.

@method_decorator(SignIn_required,name="dispatch")
class AlbumCreateView(View):
    
    def get(self,request,*args, **kwargs):
        
        form_instance=AlbumForm()
        
        qs=Album.objects.all()
        
        return render(request,"album_add.html",{"form":form_instance,"albums":qs})
    
    def post(self,request,*args, **kwargs):
        
        form_instance=AlbumForm(request.POST,files=request.FILES)
        
        if form_instance.is_valid():
            
            form_instance.save()
            
            return redirect("album-all")
        
        else:
            
            return render(request,"album_add.html",{"form":form_instance})
        
    
@method_decorator(SignIn_required,name="dispatch")

class AlbumListView(View):
    
    def get(self,request,*args, **kwargs):
        
        
        qs=Album.objects.all()
        
        return render(request,"album_list.html",{"albums":qs})
    

@method_decorator(SignIn_required,name="dispatch")

class AlbumUpdateView(View):
    
    def get(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        
        album_object=Album.objects.get(id=id)
        
        form_instance=AlbumForm(instance=album_object)
        
        return render(request,"album_edit.html",{"form":form_instance})
    
    def post(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        
        album_object=Album.objects.get(id=id)
        
        form_instance=AlbumForm(request.POST,instance=album_object,files=request.FILES)
        
        if form_instance.is_valid():
            
            form_instance.save()
            
            return redirect("album-all")
        
        else:
            
            return render(request,"album_edit.html",{"form":form_instance})

@method_decorator(SignIn_required,name="dispatch")
      
class AlbumDeleteView(View):
    
    def get(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        
        Album.objects.get(id=id).delete()
        
        return redirect("album-all")
            
 
@method_decorator(SignIn_required,name="dispatch")
           
class SongCreateView(View):
    
    def get(self,request,*args, **kwargs):
        
        form_instance=SongsForm()
        
        return render(request,"song_create.html",{"form":form_instance})
    
    def post(self,request,*args, **kwargs):
        
        form_instance=SongsForm(request.POST)
        
        if form_instance.is_valid():
            
            form_instance.save()
            
            return redirect("song-all")
        
        else:
            
            return render(request,"song_create.html",{"form":form_instance})
  
@method_decorator(SignIn_required,name="dispatch")
      
class SongListView(View):
    
    def get(self,request,*args, **kwargs):
        
        qs=Songs.objects.all()
        
        return  render(request,"song_list.html",{"songs":qs})


@method_decorator(SignIn_required,name="dispatch")
    
class SongUpdateView(View):
    
    def get(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        
        song_object=Songs.objects.get(id=id)
        
        form_instance=SongsForm(instance=song_object)
        
        return render(request,'song_edit.html',{'form':form_instance})
    
    def post(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        
        song_object=Songs.objects.get(id=id)
        
        form_instance=SongsForm(request.POST,instance=song_object)
        
        if form_instance.is_valid():
            
            form_instance.save()
        
            return redirect("song-all")
        else:
            
             return render(request,'song_edit.html',{'form':form_instance})
         

@method_decorator(SignIn_required,name="dispatch")
        
class SongDeleteView(View):
    
    def get(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        
        qs=Songs.objects.get(id=id).delete()
        
        return redirect("song-all")

@method_decorator(SignIn_required,name="dispatch")
   
class AlbumDetailView(View):
    
    def get(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        
        qs=Songs.objects.filter(album_object=id).all()
        
        qs1=Album.objects.get(id=id)
        
        return render(request,"album_detail.html",{"details":qs,"albumdetail":qs1})
    
class SignUpView(View):
    
    def get(self,request,*args, **kwargs):
        
        form_instance=RegistrationForm()
        
        return render(request,"signup.html",{"form":form_instance})
    
    def post(self,request,*args, **kwargs):
        
        form_instance=RegistrationForm(request.POST)
        
        if form_instance.is_valid():
            
            form_instance.save()
            
            messages.success(request,"Created Account Successfully")
            
            return redirect("sign-up")
        
        messages.error(request,"Invalid Input")
        
        return render(request,"signup.html",{"form":form_instance})
    
class SignInView(View):
    
    def get(self,request,*args, **kwargs):
        
        form_instance=SignInForm()
        
        return render(request,"login.html",{"form":form_instance})
    
    def post(self,request,*args, **kwargs):
        
        form_instance=SignInForm(request.POST)
        
        if form_instance.is_valid():
            
            data=form_instance.cleaned_data
            
            user_obj=authenticate(request,**data)
            
            if user_obj:
                
                login(request,user_obj)
                
                return redirect("album-all")
        
        messages.error(request,"Invalid Username or Password")
            
        return render(request,"login.html",{"form":form_instance})   
    
class SignOutView(View):
    
    def get(self,request,*args, **kwargs):
        
        logout(request)
        
        messages.success(request,"Logout Successfull")
        
        return redirect("sign-in")
 
