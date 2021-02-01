from django.db import models

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# def validate_mobile(value):
#     k=0
#     val=value
#     while value !=0:
#         value=value//10
#         k+=1
#
#     if k!=10:
#         raise ValidationError(
#             _('%(value) is not a valid Mobile number'),
#             params={'value': val},
#             )
#
# # check_email = 'sample@gmail.com'
# # def validate_email(value):
# #     check_email =value
#
# # def validate_verifyemail(value):
# #     if check_email != value:
# #         raise ValidationError(
# #             _('%(value) is not a valid email '),
# #             params={'value': value},
# #             )
#
# def validate_pan(value):
#         for i in range(10):
#             if ((i<=4 or i==9) and (value[i]>='A' and value[i]<='Z')):
#                 pass
#             elif ((i>=5 and i<=8) and (value[i]>='0' and value[i]<='9')):
#                 pass
#             else:
#                 raise ValidationError(
#                     _('%(value) is not a valid PAN number'),
#                     params={'value': value},
#                     )
# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    verify_email = models.EmailField(max_length=20,)
    mobile_no = models.IntegerField()
    pan_no = models.CharField( max_length=10, )
    dob = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.name

class Lenden(models.Model):
    name = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    principal = models.IntegerField()
    rate = models.FloatField()
    time = models.IntegerField()
    total_amount = models.FloatField()
