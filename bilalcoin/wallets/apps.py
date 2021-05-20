from __future__ import absolute_import

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WalletsConfig(AppConfig):
    name = 'bilalcoin.wallets'
    verbose_name = _("Wallets ID")

    def ready(self):
        try:
            import bilalcoin.wallets.signals  # noqa F401
        except ImportError:
            pass
