from django import forms
from django.contrib.auth.models import User
from .models import Order, Customer, RatingStar, Rating
from captcha.fields import CaptchaField


class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order_date'].label = 'Date of receipt of the order'
        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''
        self.fields['phone'].label = ''
        self.fields['address'].label = ''
        self.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': 'Name'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'placeholder': 'Surname'})
        self.fields['phone'].widget = forms.TextInput(attrs={'placeholder': 'Number phone'})
        self.fields['address'].widget = forms.TextInput(attrs={'placeholder': 'Address'})

    order_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Order
        fields = (
            'first_name', 'last_name', 'phone', 'address', 'buying_type', 'order_date', 'comment'
        )

#


class LoginForm(forms.ModelForm):

    required_css_class = "required-field"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['password'].label = ''
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Username'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'User with login {username} not found in the system.')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError("Invalid password")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']


class RegistrationForm(forms.ModelForm):

    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))
    phone = forms.CharField(required=False)
    address = forms.CharField(required=False)
    captcha = CaptchaField(required=True, label='', error_messages={'invalid': "Error confirmation code"})

    required_css_class = "field"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''
        self.fields['username'].label = ''
        self.fields['email'].label = ''
        self.fields['password'].label = ''
        self.fields['confirm_password'].label = ''
        self.fields['phone'].label = ''
        self.fields['address'].label = ''
        self.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': 'Name'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'placeholder': 'Surname'})
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Username'})
        self.fields['email'].widget = forms.TextInput(attrs={'placeholder': 'Email'})
        self.fields['phone'].widget = forms.TextInput(attrs={'placeholder': 'Number phone'})
        self.fields['address'].widget = forms.TextInput(attrs={'placeholder': 'Address'})

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError(f'Password mismatch')
        return self.cleaned_data

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'The {username} is taken')
        return username

    def clean_email(self):

        email = self.cleaned_data['email']
        marks = email.split('.')[-1]
        if marks in ['net']:
            raise forms.ValidationError(f'Registration with such marks "{marks}" is not possible')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'The e-mail address is registered in the system')
        return email

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'confirm_password', 'phone', 'address']


class ChangeIconForm(forms.ModelForm):

    icon = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['icon'].label = 'Icon'

    class Meta:
        model = User
        fields = ['icon']


class ChangeSequenceForm(forms.ModelForm):
    sequence = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sequence'].label = 'Sequence'

    class Meta:
        model = User
        fields = ['sequence']


class ChangeInformationForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your new name'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your new surname'}))
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your new number phone'}))
    address = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your new address'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''
        self.fields['phone'].label = ''
        self.fields['address'].label = ''

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone', 'address']


class RatingForm(forms.ModelForm):

    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)






