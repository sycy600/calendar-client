from django import template
import dateutil.parser
from dateutil import tz

register = template.Library()


@register.filter
def rfc3339_to_datetime(rfc3339):
    utcdatetime = dateutil.parser.parse(rfc3339)
    utc_zone = tz.tzutc()
    return utcdatetime.astimezone(utc_zone)
