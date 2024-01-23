from django.db import models
from unit.models import Unit


class Section(models.Model):
    class Meta:
        verbose_name = "Rozdział"
        verbose_name_plural = "M.03 - Rozdziały"
        ordering = ["section"]

    section = models.CharField(verbose_name="Rozdział", max_length=5, unique=True)
    name = models.CharField(verbose_name="Nazwa", max_length=20)

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
        verbose_name_plural = "M.04 - Grupy"

    group = models.IntegerField(verbose_name="Grupa", unique=True)
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
        verbose_name_plural = "M.05 - Paragrafy i pozycje"

    paragraph = models.CharField("Paragraf", max_length=7, unique=True)
    name = models.CharField("Nazwa", max_length=150)

    @classmethod
    def create_paragraphs(cls):
        data = [
            {'paragraph': '4270-01', 'name': 'Remonty'},
            {'paragraph': '4270-02', 'name': 'Konserwacje, awarie'},
            {'paragraph': '6050-03', 'name': 'Inwestycje'},
            {'paragraph': '6060-10', 'name': 'Zakupy inwestycyjne'},
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
        verbose_name_plural = "M.06 - Źródła finansowania"

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
        verbose_name_plural = "M.07 - Konta"

    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name="Rozdział")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Grupa")
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE, verbose_name="Paragraf")
    source = models.ForeignKey(Source, on_delete=models.CASCADE, verbose_name="Źródło finansowania")

    def __str__(self):
        return f"{self.section.section}-{self.group.group}-{self.paragraph}-{self.source}"


class PriorityModel(models.Model):
    class Meta:
        verbose_name = 'Priorytet'
        verbose_name_plural = 'M.08 - Priorytety'

    name = models.CharField(verbose_name='Priorytet', max_length=3)

    @classmethod
    def create_priority(cls):
        data = [
            {'name': 'I'},
            {'name': 'II'},
            {'name': 'III'},
        ]

        for item in data:
            priority = cls(name=item['name'])
            priority.save()

        return cls.objects.all()

    def __str__(self):
        return f"{self.name}"


class PlanModel(models.Model):
    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'M.01 - Plany'
        ordering = ['date']

    related_name = 'plan'

    title = models.CharField(verbose_name='Tytuł', max_length=200, null=False)
    subtitle = models.CharField(verbose_name='Podtytuł', max_length=200, null=False)
    date = models.DateField(verbose_name='Data')
    tasks_cost = models.DecimalField(verbose_name='Suma', max_digits=10, decimal_places=2)
    create = models.DateTimeField(verbose_name="Utworzenie", auto_now_add=True)
    change = models.DateTimeField(verbose_name="Zmiany", auto_now=True)
    author = models.ForeignKey(to="auth.User", on_delete=models.CASCADE, verbose_name="Autor")

    def __str__(self):
        return f"{self.title} z dnia {self.date.strftime('%d.%m.%Y')}r."


class ItemPlanModel(models.Model):
    class Meta:
        verbose_name = 'Zadanie w planie'
        verbose_name_plural = 'M.02 - Zadania w planie'
        ordering = ['create']

    related_name = 'itemPlan'

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name="Jednostka")
    task = models.CharField(verbose_name='Nazwa zadania', max_length=200, null=False)
    source = models.ForeignKey(FinanceSource, verbose_name='Źródło finansowania', on_delete=models.CASCADE,
                               related_name=related_name)
    cost = models.DecimalField(verbose_name='Szacowany koszt', max_digits=10, decimal_places=2, null=False)
    priority = models.ForeignKey(PriorityModel, verbose_name='Priorytet', on_delete=models.CASCADE,
                                 related_name=related_name)
    plan = models.ForeignKey(PlanModel, verbose_name='Plan', on_delete=models.CASCADE, related_name=related_name)
    create = models.DateTimeField(verbose_name="Utworzenie", auto_now_add=True)
    change = models.DateTimeField(verbose_name="Zmiany", auto_now=True)
    author = models.ForeignKey(to="auth.User", on_delete=models.CASCADE, verbose_name="Autor")

    def __str__(self):
        return f"{self.unit.type.type_short} {self.unit.city} - {self.task}"
