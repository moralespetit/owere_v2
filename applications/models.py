from django.db import models, connection


SEQUENCE_AUDIT_OID = "SEQ_AUDIT_OID"


def sequence_audit_oid():
  with connection.cursor() as cursor:
    cursor.execute("""SELECT nextval('SEQ_AUDIT_OID')""")
    return cursor.fetchone()[0]


class Company(models.Model):
    #oid = models.AutoField('oid', primary_key=True, editable=False)
    ref = models.CharField('ref', max_length=50, unique=True, null=False)
    name = models.CharField('name', max_length=200, null=False)
    urlLogo = models.URLField('url_Logo', max_length=255, null=True)
    #urlLogo = models.ImageField('url_Logo', max_length=255, null=True)
    active = models.BooleanField('active', default=True, null=False)
    oidAudit = models.BigIntegerField('oidAudit', default=sequence_audit_oid, editable=False)

    def __str__(self):
        return str(self.oid) + ' - ' + str(self.id) + ' - ' + self.name


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
    oidAudit = models.BigIntegerField('oidAudit', default=sequence_audit_oid, editable=False)

    def __str__(self):
        return str(self.oid) + ' - ' + str(self.id) + ' - ' + self.name + ' - ' + self.surname1
