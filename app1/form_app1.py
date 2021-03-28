from django import forms

CHOICES = [('0', 'male'), ('1', 'female'), ('2', 'other')]

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
    FullName = forms.CharField(label="Full Name", max_length=500, widget=forms.TextInput(attrs={
                                'class':"form-control",
                                'placeholder':"Enter Username"}))
    usrName=forms.CharField(label="Username",max_length=50,
                            widget=forms.TextInput(attrs={
                                'class':"form-control",
                                'placeholder':"Enter Username"}))
    emailId=forms.EmailField(label="Email id",max_length=50, 
                             widget=forms.TextInput(
                                       attrs={'class':"form-control",
                                       'aria-describedby':"emailHelp",
                                       'placeholder':"Enter Email"}))
    gender=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
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
    insta_link = forms.CharField(label='Instagram_Link', widget=forms.TextInput(
                                        attrs={'class':"form-control",
                                        'placeholder':"Enter Your Instagram Link"}))
    fb_link = forms.CharField(label='Facebook_Link', widget=forms.TextInput(
                                        attrs={'class':"form-control",
                                        'placeholder':"Enter Your Facebook Link"}))

BOOK_CHOICES = [
    ('b_action', 'Action'),
    ('b_drama', 'Drama'),
    ('b_romance', 'Romance'),
    ('b_horror', 'Horror'),
    ('b_Sci_Fi', 'Sci_Fi'),
    ('b_informative', 'Informative'),
    ('b_adventure', 'Adventure'),
    ('b_thriller', 'Thriller'),
    ('b_fictional', 'Fictional'),
    ('b_fantasy', 'Fantasy'),
    ('b_inspirational', 'Inspirational'),
    ('b_biographies', 'Biographies'),
] 

class registerForm_1(forms.Form):
    book_choices = forms.MultipleChoiceField(
        label="Select the types of books you like",
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