from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models.fields import PageField

from cms.models import Page

class CMSRedirect(models.Model):
    page = PageField(verbose_name=_("page"), blank=True, null=True, help_text=_("A link to a page has priority over a text link."))
    site = models.ForeignKey(Site)
    old_path = models.CharField(_('redirect from'), max_length=200, db_index=True,
        help_text=_("This should be an absolute path, excluding the domain name. Example: '/events/search/'."))
    new_path = models.CharField(_('redirect to'), max_length=200, blank=True,
        help_text=_("This can be either an absolute path (as above) or a full URL starting with 'http://'."))

    class Meta:
        verbose_name = _('redirect')
        verbose_name_plural = _('redirects')
        db_table = 'django_redirect'
        unique_together=(('site', 'old_path'),)
        ordering = ('old_path',)
    
    def __unicode__(self):
        return "%s ---> %s" % (self.old_path, self.new_path)