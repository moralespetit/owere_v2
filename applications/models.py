from django.db import models, connection

from applications.model import *

'''
class User(models.Model ):
    #oid = models.AutoField('oid', primary_key=True, editable=False)
    company = models.ForeignKey(Company, on_delete=models.RESTRICT, null=False)
    ref = models.CharField('ref', max_length=50, null=False)
    name = models.CharField('name', max_length=50)
    surname1 = models.CharField('surname1', max_length=50, null=True)
    surname2 = models.CharField('surname2', max_length=50, null=True)
    email = models.EmailField('email', null=False)
    phone = models.CharField('phone', max_length=15)
    active = models.BooleanField('active', default=True, null=False)
    password = models.CharField('password', max_length=256, null=True)
    oidAudit = models.BigIntegerField('oidAudit', default=getSequenceAuditOid, editable=False)

    def __str__(self):
        return str(self.oid) + ' - ' + str(self.id) + ' - ' + self.name + ' - ' + self.surname1
'''