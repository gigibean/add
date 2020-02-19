from django import forms
#from .social_models import TrackPost
from .models import Posts, Tracks, Comments



class PostForm(forms.ModelForm):
    contents = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
            attrs={'placeholder': "곡 정보를 입력하세요",
                   "class": "form-control"}
        ),
        label='desc',
        help_text='정보입력란'
    )

    class Meta:
        # model = TrackPost
        model = Posts
        fields = ('contents', 'tags', 'users_idx', 'track_idx')

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data("content")
        if content == "":
            raise forms.ValidationError("Cannot be blank")
        return content


class TrackForm(forms.ModelForm):

    class Meta:
        model = Tracks
        fields = ('title', 'type_idx', 'moods', 'genre_idx')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('users_idx', 'contents', )


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    source = forms.CharField(
        max_length=50,
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        message = cleaned_data.get('message')
        if not name and not message:
            raise forms.ValidationError('You have to write something!')
