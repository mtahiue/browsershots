from shotserver04.xmlrpc import signature
from shotserver04.factories.models import Factory
from shotserver04.requests.models import Request


@signature(str, str)
def features(request, factory_name):
    """
    Generate SQL WHERE clause to match requests for this factory.

    Arguments
    ~~~~~~~~~
    * factory_name string (lowercase, normally from hostname)

    Return value
    ~~~~~~~~~~~~
    * where string (SQL WHERE clause)
    """
    factory = Factory.objects.get(name=factory_name)
    joins, where, params = factory.features_q().get_sql(Request._meta)
    where = ' AND '.join(where)
    return where % tuple(params)