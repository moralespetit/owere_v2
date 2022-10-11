from django.core.exceptions import ValidationError
from django.db import models
from .genericModel import getSequenceAuditOid
from .company import Company
from rest_framework import serializers


class Client(models.Model):
    #oid = models.AutoField('oid', primary_key=True, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=False)
    ref = models.CharField('ref', max_length=50, unique=False, null=False)
    name = models.CharField('name', max_length=200, null=False)
    notes = models.TextField('notes', null=True, blank=True)
    active = models.BooleanField('active', default=True, null=False)
    oidAudit = models.BigIntegerField('oidAudit', default=getSequenceAuditOid, editable=False)

    class Meta:
        # database
        db_table = "CLIENT"  # name table in database
        # admin
        verbose_name = 'Cliente'  # literal name shows in Admin Screen
        ordering = ['ref'] # sort by field selected
        unique_together = ['company_id','ref'] # validate only unique combinations ('id','ref')

    def __str__(self):
        return self.ref + ' - ' + self.name

'''
    def validate_unique(self, *args, **kwargs):
        super().validate_unique(*args, **kwargs)
        unique = Client.objects.filter(company_id=self.company_id).filter(ref=self.ref)
        if unique is not None :
            raise ValidationError("item already exists")
'''

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = (
            'id','ref', 'name','notes', 'active',
        )
        #fields = ('__all__') todos los campos de client

