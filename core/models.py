from django.db import models


class SiteConfig(models.Model):
    site_name = models.CharField("Nome do site", max_length=100, default="Doula Malú")
    hero_title = models.CharField("Título principal (hero)", max_length=200, default="Eu sou Malú Gomes")
    hero_subtitle = models.CharField("Subtítulo (hero)", max_length=200, default="Educadora Perinatal")
    hero_image = models.ImageField("Foto de fundo do hero", upload_to="uploads/", blank=True, null=True)
    hero_profile_image = models.ImageField("Foto de perfil no hero (opcional)", upload_to="uploads/", blank=True, null=True)
    hero_cta_text = models.CharField("Texto do botão hero", max_length=100, default="Conheça meu trabalho", blank=True)

    about_name = models.CharField("Nome completo", max_length=200, default="Malú Bezerra Gomes")
    about_phone = models.CharField("Telefone", max_length=30, default="(84) 98880-8252")
    about_photo = models.ImageField("Foto do perfil", upload_to="uploads/", blank=True, null=True)
    about_whatsapp = models.CharField("Link WhatsApp", max_length=200, default="https://wa.me/5584988802252")
    about_instagram = models.CharField("Link Instagram", max_length=200, default="https://instagram.com/doulamalu")
    about_quote = models.TextField("Citação de destaque", default="\u201cPara mudar o mundo é preciso mudar a forma de nascer\u201d.")
    about_quote_author = models.CharField("Autor da citação", max_length=100, default="— Michael Odent")

    services_title = models.CharField("Título seção Serviços", max_length=100, default="Serviços")
    portfolio_title = models.CharField("Título CTA portfólio", max_length=200, default="Interessou-se pelo meu trabalho?")
    portfolio_text = models.TextField("Texto CTA portfólio", default="Clique no botão abaixo para baixar meu portfólio.")
    portfolio_button_text = models.CharField("Texto do botão", max_length=100, default="Baixar portfólio")
    portfolio_file = models.FileField("Arquivo do portfólio (PDF)", upload_to="uploads/", blank=True, null=True)
    portfolio_bg_image = models.ImageField("Imagem de fundo CTA", upload_to="uploads/", blank=True, null=True)

    contact_address = models.CharField("Endereço", max_length=300, default="Av. Ayrtoon Senna, 1823 - Nova Parnamirim, RN")
    contact_phone = models.CharField("Telefone contato", max_length=30, default="(84) 98880-8252")
    contact_email = models.EmailField("E-mail", default="malubezarragomes21@gmail.com")

    class Meta:
        verbose_name = "Configuração do Site"
        verbose_name_plural = "Configuração do Site"

    def __str__(self):
        return "Configuração do Site"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class AboutParagraph(models.Model):
    text = models.TextField("Parágrafo")
    highlight = models.BooleanField("Destaque (cor diferente)", default=False)
    order = models.PositiveIntegerField("Ordem", default=0)
    active = models.BooleanField("Ativo", default=True)

    class Meta:
        verbose_name = "Parágrafo — Sobre mim"
        verbose_name_plural = "Parágrafos — Sobre mim"
        ordering = ["order"]

    def __str__(self):
        return f"Parágrafo {self.order}: {self.text[:60]}..."


class Service(models.Model):
    title = models.CharField("Título do serviço", max_length=200)
    icon = models.ImageField("Ícone", upload_to="uploads/", blank=True, null=True)
    order = models.PositiveIntegerField("Ordem", default=0)
    active = models.BooleanField("Ativo", default=True)

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"
        ordering = ["order"]

    def __str__(self):
        return self.title


class ServiceParagraph(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="paragraphs", verbose_name="Serviço")
    text = models.TextField("Parágrafo")
    order = models.PositiveIntegerField("Ordem", default=0)

    class Meta:
        verbose_name = "Parágrafo do Serviço"
        verbose_name_plural = "Parágrafos do Serviço"
        ordering = ["order"]

    def __str__(self):
        return f"{self.text[:60]}"


class Photo(models.Model):
    image = models.ImageField("Foto", upload_to="uploads/")
    caption = models.CharField("Legenda", max_length=200, blank=True)
    order = models.PositiveIntegerField("Ordem", default=0)
    active = models.BooleanField("Ativo", default=True)

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"
        ordering = ["order"]

    def __str__(self):
        return self.caption or f"Foto {self.pk}"


class ContactParagraph(models.Model):
    text = models.TextField("Parágrafo")
    order = models.PositiveIntegerField("Ordem", default=0)
    active = models.BooleanField("Ativo", default=True)

    class Meta:
        verbose_name = "Parágrafo — Contatos"
        verbose_name_plural = "Parágrafos — Contatos"
        ordering = ["order"]

    def __str__(self):
        return f"Parágrafo {self.order}: {self.text[:60]}"
