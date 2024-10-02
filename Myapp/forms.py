from django import forms
from Myapp.models import Album,Songs
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AlbumForm(forms.ModelForm):
    
    class Meta:
        
        model=Album
        
        fields=["title","year","director","language","image"]
        
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            
            "year":forms.NumberInput(attrs={"class":"form-control"}),
            
            "director":forms.TextInput(attrs={"class":"form-control"}),
            
            "language":forms.TextInput(attrs={"class":"form-control"}),
            
            "image":forms.FileInput(attrs={"class":"form-control my-3"})
        }
        
class SongsForm(forms.ModelForm):
    class Meta:
        
        model=Songs
        
        fields=["title","singer","track_number","album_object"]
        
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            
            "singer":forms.TextInput(attrs={"class":"form-control"}),
            
            "track_number":forms.NumberInput(attrs={"class":"form-control"}),
            
            "album_object":forms.Select(attrs={"class":"form-control form-select"})
        }
        
class RegistrationForm(UserCreationForm):
    
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
    class Meta:
        
        model=User
        
        fields=["username","email","password1","password2"]
        
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"})
        }
        
class SignInForm(forms.Form):
    
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))