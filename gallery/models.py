from django.db import models
import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver
import os


# def upload_gallery(instance, filename):
#     new_filename = create_name_photo(instance, filename)
#     title = instance.gallery.project.project_title
#     new_title = title.replace(" ", "_")
#     return f"investments/{new_title}/gallery/{instance.gallery.name}/{new_filename}"




# Create your models here.
class GalleryModel(models.Model):
    class Meta:
        verbose_name = "Galeria"
        verbose_name_plural = "M.01 - Galerie"
        ordering = ["-name"]

    # project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="gallery", verbose_name="Projekt INW")
    name = models.DateField("Nazwa galerii")
    add_date = models.DateField("Data dodania", auto_now_add=True)
    author = models.ForeignKey("auth.user", on_delete=models.CASCADE, related_name="gallery", verbose_name="Autor")

    def __str__(self):
        return f"{self.project} ({self.name.strftime('%d.%m.%Y')})"


class PhotoModel(models.Model):
    class Meta:
        verbose_name = "Zdjęcie"
        verbose_name_plural = "M.02 - Zdjęcia"
        ordering = ["add_date"]

    gallery = models.ForeignKey(GalleryModel, on_delete=models.CASCADE, related_name="photo", verbose_name="Galeria")
    # src = models.ImageField("Zdjęcie", upload_to=upload_gallery, max_length=300)
    add_date = models.DateField("Data dodania", auto_now_add=True)

    def __str__(self):
        return f"Zdjecie dodane: {self.add_date.strftime('%d.%m.%Y')} - Galeria: {self.gallery} - Jednostka: {self.gallery.project.unit}"

# def now_date():
#     return datetime.datetime.now()
# # @receiver(pre_save, sender=Photo)
#
# def create_name_photo(instance, filename):
#     extension = filename.split(".")[-1]
#     datetime = now_date()
#     date = datetime.strftime("%Y-%m-%d_(%H:%M:%S:%f)")
#     # file = os.path.splitext(filename)
#     new_filename = f"{instance.gallery.project.unit.city}_{date}.{extension}"
#
#     return new_filename
