from django import forms
from .models import Post,Category, Comment

# choices = [('coding','coding'),('sports','sports'),('entertainment','entertainment'),]
choices = Category.objects.all().values_list('name','name')
choice_list = []
for item in choices:
    choice_list.append(item)

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','body','snippet', 'header_image')
        widgets ={
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class':'form-control'}),
            # 'author' : forms.TextInput(attrs={'class':'form-control','value':'','id':'author','disabled':''}),
            'author' : forms.Select(attrs={'class':'form-control','id':'author'}),
            'category' : forms.Select(choices = choice_list, attrs={'class':'form-control', 'id' : 'category'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
            'snippet' : forms.Textarea(attrs={'class':'form-control'}),
            'header_image' : forms.FileInput(attrs={'class':'form-control'}),
        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','body','snippet', 'header_image')
        widgets ={
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class':'form-control'}),
            # 'author' : forms.TextInput(attrs={'class':'form-control','value':'','id':'author','disabled':''}),
            'author' : forms.Select(attrs={'class':'form-control','id':'author'}),
            'category' : forms.Select(choices = choice_list, attrs={'class':'form-control', 'id' : 'category'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
            'snippet' : forms.Textarea(attrs={'class':'form-control'}),
            'header_image' : forms.ClearableFileInput(attrs={'class':'form-control'}),
        }

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets ={
            'body' : forms.Textarea(attrs={'class':'form-control'}),
        }