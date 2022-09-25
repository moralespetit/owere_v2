from django.db import models
from .genericModel import getSequenceAuditOid


class Company(models.Model):
    #oid = models.AutoField('oid', primary_key=True, editable=False)
    ref = models.CharField('ref', max_length=50, unique=True, null=False)
    name = models.CharField('name', max_length=200, null=False)
    urlLogo = models.URLField('url_Logo', max_length=255, null=True)
    #urlLogo = models.ImageField('url_Logo', max_length=255, null=True)
    active = models.BooleanField('active', default=True, null=False)
    oidAudit = models.BigIntegerField('oidAudit', default=getSequenceAuditOid, editable=False)

    class Meta:
        verbose_name = 'Empresas'  # literal name shows in Admin Screen
        db_table = "COMPANY"  # name table in database

    def __str__(self):
        return str(self.oid) + ' - ' + str(self.id) + ' - ' + self.name