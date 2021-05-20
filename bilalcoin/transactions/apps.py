from __future__ import absolute_import

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TransactionsConfig(AppConfig):
    name = 'bilalcoin.transactions'
    verbose_name = _("Transactions")

    def ready(self):
        try:
            import bilalcoin.users.signals  # noqa F401
        except ImportError:
            pass
