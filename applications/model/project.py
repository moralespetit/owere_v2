from django.db import models

from applications.model.client import Client
from applications.model import getSequenceAuditOid


class ProjectStatus (models.Model):
    #oid
    pid = models.CharField('pid', max_length=255, null=False)
    descr = models.TextField('descr', max_length=2048)
    oidAudit = models.BigIntegerField('oidAudit', default=getSequenceAuditOid, editable=False)


class Project (models.Models):
    #oid
    client = models.ForeignKey(Client, null=False)
    pid = models.CharField('pid', max_length=255, null=False)
    numProj = models.CharField('numProj', max_length=255)
    numClientProj = models.CharField('numClientProj', max_length=255)
    title = models.CharField('title', max_length=255)
    descr = models.TextField('descr', max_length=4096)
    status = models.ForeignKey(ProjectStatus, null=False)
    oidAudit = models.BigIntegerField('oidAudit', default=getSequenceAuditOid, editable=False)


