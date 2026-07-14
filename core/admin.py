from django.contrib import admin
from django.utils.html import format_html
from .models import SiteConfig, AboutParagraph, Service, ServiceParagraph, Photo, ContactParagraph


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    fieldsets = (
        ("🏠 Início (Hero)", {
            "fields": ("site_name", "hero_title", "hero_subtitle", "hero_image", "hero_profile_image", "hero_cta_text"),
        }),
        ("👤 Sobre Mim — Dados", {
            "fields": ("about_name", "about_phone", "about_photo", "about_whatsapp", "about_instagram", "about_quote", "about_quote_author"),
        }),
        ("🛎 Serviços", {
            "fields": ("services_title",),
        }),
        ("📁 Portfólio", {
            "fields": ("portfolio_title", "portfolio_text", "portfolio_button_text", "portfolio_file", "portfolio_bg_image"),
        }),
        ("📞 Contatos — Dados", {
            "fields": ("contact_address", "contact_phone", "contact_email"),
        }),
    )

    def has_add_permission(self, request):
        return not SiteConfig.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(AboutParagraph)
class AboutParagraphAdmin(admin.ModelAdmin):
    list_display = ("short_text", "order", "highlight", "active")
    list_editable = ("order", "highlight", "active")
    ordering = ("order",)

    def short_text(self, obj):
        return obj.text[:80] + "..." if len(obj.text) > 80 else obj.text
    short_text.short_description = "Texto"


class ServiceParagraphInline(admin.TabularInline):
    model = ServiceParagraph
    extra = 1
    fields = ("text", "order")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "active", "icon_preview")
    list_editable = ("order", "active")
    ordering = ("order",)
    inlines = [ServiceParagraphInline]

    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<img src="{}" style="height:40px"/>', obj.icon.url)
        return "-"
    icon_preview.short_description = "Ícone"


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("__str__", "order", "active", "photo_preview")
    list_editable = ("order", "active")
    ordering = ("order",)

    def photo_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:60px; border-radius:4px"/>', obj.image.url)
        return "-"
    photo_preview.short_description = "Preview"


@admin.register(ContactParagraph)
class ContactParagraphAdmin(admin.ModelAdmin):
    list_display = ("short_text", "order", "active")
    list_editable = ("order", "active")
    ordering = ("order",)

    def short_text(self, obj):
        return obj.text[:80] + "..." if len(obj.text) > 80 else obj.text
    short_text.short_description = "Texto"
