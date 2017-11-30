from django.conf.urls import include, url
from billing import get_integration

pay_pal = get_integration("pay_pal")
fps = get_integration("amazon_fps")
braintree = get_integration("braintree_payments")

urlpatterns = [
      url('^paypal-ipn-url/', include(pay_pal.urls)),
      url('^fps/', include(fps.urls)),
      url('^braintree/', include(braintree.urls)),
]
