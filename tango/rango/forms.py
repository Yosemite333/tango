#-*-coding:utf-8-*-
from django import forms
from rango.models import Page, Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length = 128, help_text = 'Bu alana bir kategori ismi giriniz')
    views = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    likes = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)

    # form sınıfı ile ilgili ek bilgi sağlıyor
    class Meta:
        # bir model ve bir ModelForm arasında ilişki sağlıyor
        model = Category

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length = 128, help_text = 'Bu alana sayfanın başlığını yazınız!')
    url = forms.URLField(max_length = 200, help_text = 'Bu alana bir internet adresi yazınız!')
    views = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    
    class Meta:
        model = Page
        # bir model içerisinde yer alan alanların hepsinin değil 
        # sadece bir kısmının form içerisinde listelenmesini sağlamak için fields 
        # kullanılıyor. 
        fields = ('title', 'url', 'views')

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
        return cleaned_data
