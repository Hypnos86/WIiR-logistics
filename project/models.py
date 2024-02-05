from django.db import models
from unit.models import Unit


class ContractorModel(models.Model):
    class Meta:
        verbose_name = "Kontrahent"
        verbose_name_plural = "M.01 - Kontrahenci"
        ordering = ["name"]
        unique_together = ["nip"]

    name = models.CharField(verbose_name="Nazwa", max_length=100, null=True)
    nip = models.CharField(verbose_name="NIP", max_length=10, null=True, blank=True, unique=True)
    address = models.CharField(verbose_name="Adres", max_length=30, null=True)
    zip_code = models.CharField(verbose_name="Kod pocztowy", max_length=6, null=True)
    city = models.CharField(verbose_name="Miasto", max_length=20, null=True)
    information = models.TextField(verbose_name="Informacje", null=True, blank=True, default="")
    slug = models.SlugField(max_length=50, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    change = models.DateTimeField(verbose_name="Zmiany", auto_now=True)
    author = models.ForeignKey(to="auth.User", on_delete=models.CASCADE, verbose_name="Autor")

    def __str__(self):
        return f"{self.name}, {self.address}, {self.zip_code} {self.city}"


def upload_scan(instance, filename):
    title = instance.project_title
    new_title = title.replace(" ", "_")
    return f"project/{new_title}/{filename}"


# Create your models here.
class ProjectModel(models.Model):
    class Meta:
        verbose_name = "Inwestycyja"
        verbose_name_plural = "M.02 - Inwestycje"
        ordering = ["date_of_acceptance"]

    date_of_acceptance = models.DateField(verbose_name="Data programu", null=True, blank=True)
    no_acceptance_document = models.CharField(verbose_name="L.dz. dokumentu", max_length=15, null=True, blank=True)
    scan_program = models.FileField(upload_to=upload_scan, null=True, blank=True,
                                          verbose_name="Program inwestycji")
    project_title = models.CharField(verbose_name="Nazwa zadania", max_length=300, null=True, blank=True)
    investment_cost_estimate_value = models.DecimalField(verbose_name="WKI", max_digits=12, decimal_places=2, null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="project", verbose_name="Jednostka")
    information = models.TextField(verbose_name="Informacje", null=True, blank=True)
    date_of_settlement = models.DateField(verbose_name="Data rozliczenia", null=True, blank=True)
    scan_settlement = models.FileField(upload_to=upload_scan, null=True, blank=True,
                                       verbose_name="Rozliczenie")
    realized = models.BooleanField(verbose_name="Zrealizowane", default=False)
    creation_date = models.DateTimeField(verbose_name="Data utworzenia", auto_now_add=True)
    change = models.DateTimeField(verbose_name="Zmiana", auto_now=True)
    author = models.ForeignKey(to="auth.User", on_delete=models.CASCADE, related_name="project", verbose_name="Autor")

    def __str__(self):
        return f"{self.project_title}"

