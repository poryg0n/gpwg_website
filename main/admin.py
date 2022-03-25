from django.contrib import admin
from .models import (
        Post,
        Main,
        MainItem,
        About,
        AboutItem,
        Threat,
        ThreatItem,
        Conservation,
        ConservationItem,
        Gabon,
        GabonItem,
        FAQ,
        FAQItem,
        Action,
        ActionItem,
        PCP,
        PCPItem,
        Fund,
        FundItem,
        WPD,
        WPDItem,
        New,
        NewItem,
        Help,
        HelpItem,
        Resource,
        ResourceItem,
        Meet,
        MeetItem,
        Partner,
        PartnerItem
        )

# Register your models here.
admin.site.register(Main)
admin.site.register(MainItem)
admin.site.register(About)
admin.site.register(AboutItem)
admin.site.register(Threat)
admin.site.register(ThreatItem)
admin.site.register(Conservation)
admin.site.register(ConservationItem)
admin.site.register(Gabon)
admin.site.register(GabonItem)
admin.site.register(FAQ)
admin.site.register(FAQItem)
admin.site.register(Action)
admin.site.register(ActionItem)
admin.site.register(PCP)
admin.site.register(PCPItem)
admin.site.register(Fund)
admin.site.register(FundItem)
admin.site.register(WPD)
admin.site.register(WPDItem)
admin.site.register(New)
admin.site.register(NewItem)
admin.site.register(Help)
admin.site.register(HelpItem)
admin.site.register(Resource)
admin.site.register(ResourceItem)
admin.site.register(Meet)
admin.site.register(MeetItem)
admin.site.register(Partner)
admin.site.register(PartnerItem)
