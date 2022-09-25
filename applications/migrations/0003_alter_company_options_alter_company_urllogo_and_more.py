# Generated by Django 4.1.1 on 2022-09-25 16:17

import applications.model.genericModel
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_create_audit_seq'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['ref'], 'verbose_name': 'Empresa'},
        ),
        migrations.AlterField(
            model_name='company',
            name='urlLogo',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='', verbose_name='url_Logo'),
        ),
        migrations.AlterUniqueTogether(
            name='company',
            unique_together={('ref',)},
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=50, unique=True, verbose_name='ref')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='notes')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('oidAudit', models.BigIntegerField(default=applications.model.genericModel.getSequenceAuditOid, editable=False, verbose_name='oidAudit')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='applications.company')),
            ],
            options={
                'verbose_name': 'Cliente',
                'db_table': 'CLIENT',
                'ordering': ['ref'],
                'unique_together': {('company_id', 'ref')},
            },
        ),
    ]
