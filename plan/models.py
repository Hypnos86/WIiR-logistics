from django.db import models


class Section(models.Model):
    class Meta:
        verbose_name = "Rozdział"
        verbose_name_plural = "Rozdziały"
        ordering = ["section"]

    section = models.CharField("Rozdział", max_length=5, unique=True)
    name = models.CharField("Nazwa", max_length=20)

    @classmethod
    def create_sections(cls):
        data = [
            {'section': '75401', 'name': 'CBŚP'},
            {'section': '75402', 'name': 'BSWP'},
            {'section': '75404', 'name': 'KWP'},
            {'section': '75405', 'name': 'KMP/KPP'},
            {'section': '75407', 'name': 'CBZC'}
        ]

        for item in data:
            section = cls(section=item['section'], name=item['name'])
            section.save()
        return cls.objects.all()

    def __str__(self):
        return f"{self.section} ({self.name})"


class Group(models.Model):
    class Meta:
        verbose_name = "Grupa"
        verbose_name_plural = "K.01 - Grupy"

    group = models.IntegerField("Grupa", max_length=2, unique=True)
    name = models.CharField("Nazwa", max_length=50)

    @classmethod
    def create_groups(cls):
        data = [
            {'group': 7, 'name': 'gr.7'}
        ]
        for item in data:
            group = cls(group=item['group'], name=item['name'])
            group.save()
        return cls.objects.all()

    def __str__(self):
        return f"gr.{self.group}"


class Paragraph(models.Model):
    class Meta:
        verbose_name = "Paragraf i pozycja"
        verbose_name_plural = "K.03 - Paragrafy i pozycje"

    paragraph = models.CharField("Paragraf", max_length=7, unique=True)
    name = models.CharField("Nazwa", max_length=150)

    @classmethod
    def create_paragraphs(cls):
        data = [
            {'paragraph': '4270-01', 'name': 'Remonty z Planu remontów'},
            {'paragraph': '4270-02', 'name': 'Konserwacja pomieszczeń, buydnków i budowli'},
            {'paragraph': '6050-03', 'name': 'Wydatki inwestycyjne'},
            {'paragraph': '6060-10', 'name': 'Wydatki na zakupy inwestycyjne'},
        ]

        for item in data:
            paragraphs = cls(paragraph=item['paragraph'], name=item['name'])
            paragraphs.save()
        return cls.objects.all()

    def __str__(self):
        return f"{self.paragraph}"


class Source(models.Model):
    class Meta:
        verbose_name = "Źródło finansowania"
        verbose_name_plural = "K.04 - Źródła finansowania"

    source = models.CharField("Źródło", max_length=8, null=True)
    name = models.CharField("Źródło", max_length=100, null=True)

    @classmethod
    def create_sources(cls):
        data = [
            {'source': '100', 'name': 'KWP'},
            {'source': '400', 'name': 'BLP KGP'},
            {'source': '200', 'name': 'BLP KGP - PMP'},
        ]

        for item in data:
            sources = cls(source=item['source'], name=item['name'])
            sources.save()
        return cls.objects.all()

    def __str__(self):
        return f"{self.source}"


class FinanceSource(models.Model):
    class Meta:
        verbose_name = "Konto"
        verbose_name_plural = "K.05 - Konta"

    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name="Rozdział")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Grupa")
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE, verbose_name="Paragraf")
    source = models.ForeignKey(Source, on_delete=models.CASCADE, verbose_name="Źródło finansowania")

    def __str__(self):
        return f"{self.section.section}-{self.group.group}-{self.paragraph}-{self.source}"
