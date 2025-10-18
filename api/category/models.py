from django.db import models

class Category(models.Model):
    id_category = models.CharField(primary_key=True, max_length=10, editable=False)
    nomCategory = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.id_category:
            last = Category.objects.order_by('-id_category').first()
            if last:
                last_id_num = int(last.id_category.replace('CAT', ''))
                new_id = f'CAT{last_id_num + 1:03}'
            else :
                new_id = 'CAT001'
            self.id_category = new_id
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id_category} - {self.nomCategory}"