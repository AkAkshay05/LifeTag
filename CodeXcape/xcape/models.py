from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

class Xcape(models.Model):
    name = models.CharField(max_length=200)
    guardian_phone = models.CharField(max_length=15)
    address = models.TextField()
    blood_type = models.CharField(max_length=5)
    allergies = models.TextField(blank=True)
    description = models.TextField(blank=True)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Data to encode in QR (URL that shows detail page)
        data = f"http://127.0.0.1:8000/view/{self.id}/"

        qr_img = qrcode.make(data)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qr_img)

        fname = f'qr_code-{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()

        super().save(*args, **kwargs)
