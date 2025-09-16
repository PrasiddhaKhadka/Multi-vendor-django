from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            # You cannot create a user without an email.
            raise ValueError('The email must be set')
        
        # Converts emails into a standard format.
        # Example: 'TEST@GMAIL.COM' → 'test@gmail.com'
        email = self.normalize_email(email)
        
        
        # self.model points to your User model (which you'll define later).
         # It initializes the user object with email and any extra fields (like first_name, etc.)
        user = self.model(email=email, **extra_fields)

        user.set_password(password) # Hashes the password (never stores raw password).


        #self.db will be using default database
        user.save(using = self._db)                 # Saves user in the database. 


        return user
    

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(
            email= self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user
       
class User(AbstractBaseUser):

    RESTAURANT = 1
    CUSTOMER = 2

    ROLE_CHOICES = (
        (RESTAURANT, 'Restaurant'),
        (CUSTOMER, 'Customer')
    )
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

    # required roles 
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    
    USERNAME_FIELD = 'email'
    # donnt need to place the userfield name into required fields because it itself lies in required fields 
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    profile_pic = models.ImageField(upload_to='user/profile_pics', blank=True,null=True)
    phone = models.CharField(max_length=15, blank=True)
    address_line_1 = models.CharField(max_length=50, blank=True)
    address_line_2 = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=20, blank=True)
    longitude = models.CharField(max_length=20, blank=True)
    latitude = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email