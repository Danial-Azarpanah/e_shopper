import ghasedakpack
from decouple import config

sms = ghasedakpack.Ghasedak(config("SMS_API_KEY"))
sms.verification({'receptor': '09xxxxxxxxx', 'type': '1',
                  'template': f'{config("SMS_TEMPLATE_NAME")}', 'param1': '1234'})
