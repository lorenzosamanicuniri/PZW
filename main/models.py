from django.db import models

class Proizvodjac(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField()

    def __str__(self):
        return self.name

class Plastika(models.Model):
    plastika_proizvodjac = models.ForeignKey(Proizvodjac, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slika = models.ImageField(blank=True, null=True, default="815.jpg")
    type = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    temperature = models.CharField(max_length=20)
    website = models.URLField(default="default@gmail.com")

    def __str__(self):
        return self.name    

class Printer(models.Model):
    printer_proizvodjac = models.ForeignKey(Proizvodjac, default=1, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    slikaa = models.ImageField(blank=True, null=True)
    type = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    printer_plastika = models.ManyToManyField(Plastika)
    website = models.URLField()

    def __str__(self):
        return self.model

    def get_Plastika(self):
        
        Pllastika = self.printer_plastika.all()
        Plastikaa = ""
        for post in Pllastika:
            Plastikaa+=post.name
            Plastikaa+=", "
        return Plastikaa
        
