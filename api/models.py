from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _ #
from django.conf import settings
from datetime import date

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Your custom fields and methods here

    class Meta:
        # You can specify other settings for your User model here
        # For example, if you want to use a different table name for your User model
        db_table = 'custom_user'

# To avoid the clash in reverse accessors, define related_name for groups and user_permissions
User._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_user_permissions'
