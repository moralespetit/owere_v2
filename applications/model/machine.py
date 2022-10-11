from django.db import models, connection

from applications.model import Company, Attached, getSequenceAuditOid

SEQUENCE_MACHINE_REF = "SEQ_MACHINE_REF"


def getRefMachine():
    with connection.cursor() as cursor:
        cursor.execute("SELECT nextval('"+SEQUENCE_MACHINE_REF+"')")
        return cursor.fetchone()[0]

class Machine (models.Model):
    # oid
    company = models.ForeignKey(Company, on_delete=models.RESTRICT, null=False)
    pid = models.CharField('pid', max_length=255, null=False, default=getRefMachine)
    brand = models.CharField('brand', max_length=255, null=False)
    model = models.CharField('model', max_length=255, null=False)
    ref = models.CharField('ref', max_length=255, null=False)
    tecFile = models.ForeignKey(Attached, on_delete=models.RESTRICT, null=True)
    ceCert = models.ForeignKey(Attached, on_delete=models.RESTRICT, null=True)
    calibrationCert = models.ForeignKey(Attached, on_delete=models.RESTRICT, null=True)
    active = models.BooleanField('active', default=True, null=False)
    oidAudit = models.BigIntegerField('oidAudit', default=getSequenceAuditOid, editable=False)




