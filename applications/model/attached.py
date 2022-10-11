from django.db import models
from .genericModel import getSequenceAuditOid


class Attached(models.Model):
    # oid
    file = models.FileField('file', upload_to='')
    oidAudit = models.BigIntegerField('oidAudit', default=getSequenceAuditOid, editable=False)
