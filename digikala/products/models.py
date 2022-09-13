from django.db import models


class Digikala(models.Model):
    product_id = models.IntegerField(unique=True)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=50)
    price = models.IntegerField()
    off = models.IntegerField()
    url = models.URLField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Mobile(Digikala):
    ram = models.CharField(max_length=20, blank=True)

    cpu = models.CharField(max_length=20, blank=True)

    size = models.CharField(max_length=20, blank=True)
    resolution = models.CharField(max_length=20, blank=True)

    storage = models.CharField(max_length=20, blank=True)

    network = models.CharField(max_length=20, blank=True)

    main_camera = models.CharField(max_length=20, blank=True)
    selfie_camera = models.TextField(blank=True)

    battery = models.TextField(blank=True)


class Laptop(Digikala):
    cpu_manifacturer = models.CharField(max_length=20, blank=True)
    cpu_serry = models.CharField(max_length=20, blank=True)
    cpu_model = models.CharField(max_length=20, blank=True)

    ram_capacity = models.CharField(max_length=20, blank=True)
    ram_type = models.CharField(max_length=20, blank=True)

    gpu_manifacturer = models.CharField(max_length=20, blank=True)
    gpu_model = models.CharField(max_length=20, blank=True)

    internal_sotrage_type = models.CharField(max_length=50, blank=True)

    size = models.CharField(max_length=20, blank=True)
    resolution = models.CharField(max_length=20, blank=True)

    optical_drive = models.CharField(max_length=50, blank=True)

    connection_ports = models.CharField(max_length=200, blank=True)

    usb2 = models.CharField(max_length=20, blank=True)
    usb3 = models.CharField(max_length=20, blank=True)

    battery = models.TextField(blank=True)
