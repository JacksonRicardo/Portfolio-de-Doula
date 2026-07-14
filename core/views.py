from django.shortcuts import render
from django.http import FileResponse, Http404
from .models import SiteConfig, AboutParagraph, Service, Photo, ContactParagraph


def index(request):
    config = SiteConfig.objects.first()
    about_paragraphs = AboutParagraph.objects.filter(active=True)
    services = Service.objects.filter(active=True).prefetch_related("paragraphs")
    photos = Photo.objects.filter(active=True)
    contact_paragraphs = ContactParagraph.objects.filter(active=True)
    return render(request, "core/index.html", {
        "config": config,
        "about_paragraphs": about_paragraphs,
        "services": services,
        "photos": photos,
        "contact_paragraphs": contact_paragraphs,
    })


def download_portfolio(request):
    config = SiteConfig.objects.first()
    if config and config.portfolio_file:
        return FileResponse(config.portfolio_file.open("rb"), as_attachment=True, filename="portfolio-doula-malu.pdf")
    raise Http404("Portfólio não disponível")
