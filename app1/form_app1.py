from django import forms

class loginForm(forms.Form):
    emailId=forms.EmailField(label="Email id",max_length=50, 
                             widget=forms.TextInput(
                                    attrs={'class':"form-control",
                                       'aria-describedby':"emailHelp",
                                       'placeholder':"Enter email"}))
    password=forms.CharField(widget=forms.PasswordInput(
                                        attrs={'class':"form-control",
                                        'placeholder':"Password"}))
    

class registerForm(forms.Form):
    usrName=forms.CharField(label="Username",max_length=50,
                            widget=forms.TextInput(attrs={
                                'class':"form-control",
                                'placeholder':"Enter Username"}))
    emailId=forms.EmailField(label="Email id",max_length=50, 
                             widget=forms.TextInput(
                                       attrs={'class':"form-control",
                                       'aria-describedby':"emailHelp",
                                       'placeholder':"Enter Email"}))
    password=forms.CharField(widget=forms.PasswordInput(
                                        attrs={'class':"form-control",
                                        'placeholder':"Enter Password"}))
    Confirm_password=forms.CharField(widget=forms.PasswordInput(
                                        attrs={'class':"form-control",
                                        'placeholder':"Confirm Password"}))
    age=forms.CharField(widget=forms.NumberInput(
                                        attrs={'class':"form-control",
                                        'placeholder':"Enter Age"}))
    
    phonenumber=forms.CharField(label="Contact No.", widget=forms.NumberInput(
                                        attrs={'class':"form-control",
                                        'placeholder':"Enter Contact No"}))
    
    Country=forms.CharField(label="Country",max_length=50,
                            widget=forms.TextInput(attrs={
                                'class':"form-control",
                                'placeholder':"Enter Country"}))
    
    pincode=forms.CharField(widget=forms.NumberInput(
                                        attrs={'class':"form-control",
                                        'placeholder':"Enter pincode"}))

BOOK_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
] 

class registerForm_1(forms.Form):
    book_choices = forms.MultipleChoiceField(
        label="Select the types of books     you like",
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=BOOK_CHOICES,
    )
    movie_choices = forms.MultipleChoiceField(
        label="Select the types of Movies you like",
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=BOOK_CHOICES,
    )