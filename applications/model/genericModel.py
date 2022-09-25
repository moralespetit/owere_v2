from django.db import models, connection


SEQUENCE_AUDIT_OID = "SEQ_AUDIT_OID"


def getSequenceAuditOid():
  with connection.cursor() as cursor:
    cursor.execute("""SELECT nextval('SEQ_AUDIT_OID')""")
    return cursor.fetchone()[0]