from django.contrib import admin


class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'ref', 'name', 'active',
    );


class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'get_ref_company', 'id', 'name', 'active',
    );

    def get_ref_company(self, obj):
        return obj.company.ref

    get_ref_company.short_description = 'Ref Company'

