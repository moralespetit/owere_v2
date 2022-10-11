from django.db import models

from applications.model import getSequenceAuditOid
from applications.model.machine import Machine


class MachineParams(models.Model):
    #oid
    machine = models.ForeignKey(Machine, on_delete=models.RESTRICT, null=False)
    oidAudit = models.BigIntegerField('oidAudit', default=getSequenceAuditOid, editable=False)
