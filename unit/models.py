from django.db import models
from django.utils.crypto import get_random_string
from django.utils.text import slugify


# Create your models here.
class County(models.Model):
    class Meta:
        verbose_name = "Powiat"
        verbose_name_plural = "Powiaty"
        ordering = ["id_order"]

    name = models.CharField(max_length=15, null=False, verbose_name="Powiat", unique=True)
    id_order = models.IntegerField(verbose_name="Kolejność", unique=True, null=True)

    @classmethod
    def create_county(cls):
        # Tworzenie listy danych, które mają być użyte do stworzenia obiektów
        data = [
            {"name": "KWP", "id_order": 1},
            {"name": "Chodzież", "id_order": 2},
            {"name": "Czarnków", "id_order": 3},
            {"name": "Gniezno", "id_order": 4},
            {"name": "Gostyń", "id_order": 5},
            {"name": "Grodzisk Wlkp.", "id_order": 6},
            {"name": "Jarocin", "id_order": 7},
            {"name": "Kalisz", "id_order": 8},
            {"name": "Kępno", "id_order": 9},
            {"name": "Koło", "id_order": 10},
            {"name": "Konin", "id_order": 11},
            {"name": "Kościan", "id_order": 12},
            {"name": "Krotoszyn", "id_order": 13},
            {"name": "Leszno", "id_order": 14},
            {"name": "Międzychód", "id_order": 15},
            {"name": "Nowy Tomyśl", "id_order": 16},
            {"name": "Oborniki", "id_order": 17},
            {"name": "Ostrów Wlkp.", "id_order": 18},
            {"name": "Ostrzeszów", "id_order": 19},
            {"name": "Piła", "id_order": 20},
            {"name": "Pleszew", "id_order": 21},
            {"name": "Poznań", "id_order": 22},
            {"name": "Rawicz", "id_order": 23},
            {"name": "Słupca", "id_order": 24},
            {"name": "Śrem", "id_order": 25},
            {"name": "Środa Wlkp.", "id_order": 26},
            {"name": "Szamotuły", "id_order": 27},
            {"name": "Turek", "id_order": 28},
            {"name": "Wągrowiec", "id_order": 29},
            {"name": "Wolsztyn", "id_order": 30},
            {"name": "Września", "id_order": 31},
            {"name": "Złotów", "id_order": 32},
            {"name": "CBZC", "id_order": 33},
            {"name": "CBŚP", "id_order": 34},
            {"name": "BSWP", "id_order": 35},
        ]

        # Tworzenie i zapisywanie obiektów w pętli
        for item in data:
            county = cls(name=item["name"], id_order=item["id_order"])
            county.save()

        return cls.objects.all()

    def __str__(self):
        return f"{self.name} - {self.swop_id}"


class TypeUnit(models.Model):
    class Meta:
        verbose_name = "Rodzaj jednostki"
        verbose_name_plural = "J.02 - Rodzaje jednostek"
        ordering = ["id"]

    type_short = models.CharField(max_length=10, null=False, verbose_name="Skrócona nazwa")
    type_full = models.CharField(max_length=30, null=False, verbose_name="Pełna nazwa")

    @classmethod
    def create_type_unit(cls):
        # Tworzenie listy danych, które mają być użyte do stworzenia obiektów
        data = [
            {"type_short": "CBŚP", "type_full": "Centralne Biuro Śledcze Policji", "id_order": 1},
            {"type_short": "BSWP", "type_full": "Biuro Spraw Wewnętrznych Policji", "id_order": 2},
            {"type_short": "KWP", "type_full": "Komenda Wojewódzka Policji", "id_order": 3},
            {"type_short": "KMP", "type_full": "Komenda Miejska Policji", "id_order": 4},
            {"type_short": "KPP", "type_full": "Komenda Powiatowa Policji", "id_order": 5},
            {"type_short": "KP", "type_full": "Komisariat Policji", "id_order": 6},
            {"type_short": "PP", "type_full": "Posterunek Policji", "id_order": 7},
            {"type_short": "RD", "type_full": "Rewir Dzielnicowych", "id_order": 8},
            {"type_short": "PPD", "type_full": "Punkt Przyjęć Dzielnicowych", "id_order": 9},
            {"type_short": "PPI", "type_full": "Punkt Przyjęć Interesantów", "id_order": 10},
            {"type_short": "CBZC", "type_full": "Centralne Biuro Zwalczania Cyberprzestępczości", "id_order": 11},
            {"type_short": "LK", "type_full": "Laboratorium Kryminalistyczne", "id_order": 12},
            {"type_short": "LOT", "type_full": "Lotnictwo", "id_order": 13},
            {"type_short": "Inne", "type_full": "Inne", "id_order": 14}
        ]

        # Tworzenie i zapisywanie obiektów w pętli
        for item in data:
            typeUnit = cls(type_short=item["type_short"], type_full=item["type_full"], id_order=item["id_order"])
            typeUnit.save()

        return cls.objects.all()

    def __str__(self):
        return f"{self.type_full}"


class Unit(models.Model):
    class Meta:
        verbose_name = "Jednostka"
        verbose_name_plural = "Jednostki"
        ordering = ["county__name", "type"]

    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name="unit", verbose_name="Powiat")
    type = models.ForeignKey(TypeUnit, on_delete=models.CASCADE, related_name="unit", verbose_name="Rodzaj jednostki")
    address = models.CharField(max_length=50, verbose_name="Adres")
    zip_code = models.CharField(max_length=6, verbose_name="Kod pocztowy")
    city = models.CharField(max_length=40, verbose_name="Miasto")
    manager = models.CharField(max_length=150, verbose_name="Administrator", default="Policja")
    information = models.TextField(blank=True, verbose_name="Informacja")
    status = models.BooleanField(default=True, verbose_name="Aktualna")
    full_name = models.CharField(max_length=250, verbose_name="Pełna nazwa jednostki", null=True, blank=True)
    slug = models.SlugField(max_length=80, default='', null=True)
    create = models.DateTimeField(verbose_name="Utworzenie", auto_now_add=True)
    change = models.DateTimeField(verbose_name="Zmiany", auto_now=True)
    author = models.ForeignKey(to="auth.User", on_delete=models.CASCADE, related_name="unit", verbose_name="Autor")

    def save(self, *args, **kwargs):
        # Sprawdzenie, czy pole Slug jest puste
        if not self.slug:
            # Generowanie wartości Slug na podstawie miasta i adresu
            slug = slugify(f"{self.type.type_short}-{self.city}-{self.address}-{self.id}")

            # Sprawdzenie unikalności Slug w obecnej bazie danych
            while Unit.objects.filter(slug=slug).exists():
                # Jeśli istnieje już taki Slug, dodaj losowy ciąg znaków
                random_string = get_random_string(length=4)
                slug = f"{slug}-{random_string}"

            # Przypisanie wygenerowanego Slug do pola Slug w modelu
            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.type} {self.city}, {self.address}"
