from django.db import models

from applications.model import getSequenceAuditOid
from applications.model.project import Project


class Paper(models.Model):
    #oid
    project = models.ForeignKey(Project, on_delete=models.RESTRICT, null=False)
    title = models.CharField('title', max_length=255)
    descr = models.TextField('descr', max_length=4096)
    oidAudit = models.BigIntegerField('oidAudit', default=getSequenceAuditOid, editable=False)
