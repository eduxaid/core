"""
Eduxa Course Model
@author   Sandi Andrian <sandi.andrian@eduxa.id>
@since    Apr 03, 2021
"""
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Category Status
class CategoryStatus(models.TextChoices):
    DRAFT = 'DRAFT', _('DRAFT'),
    PUBLISHED = 'PUBLISHED', _('PUBLISHED')

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    slug = models.SlugField(editable=False, unique=True)
    description = RichTextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=CategoryStatus.choices,
        default=CategoryStatus.DRAFT
    )
    parent = models.ForeignKey('Category', models.DO_NOTHING, verbose_name="Parent Category", null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'eduxa_category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
