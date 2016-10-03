from tastypie.resources import ModelResource
from tastypie.constants import ALL

from exapi1.exdb.models import Entry


class EntryResource(ModelResource):
    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'exdb'
        filtering = {'title': ALL}
