from django.db import models

# Create your models here.
class shipment_details(models.Model):
    PONumber= models.CharField(max_length=200)
    SupNam = models.CharField(max_length=200)
    SupAddress = models.CharField(max_length=200)
    Composition = models.CharField(max_length=200)
    ClothingStructure = models.CharField(max_length=200)
    MerchandiseDescription = models.CharField(max_length=200)
    PaymentCondition = models.CharField(max_length=200)
    TransportationMethod = models.CharField(max_length=200)
    DeliveryCondition = models.CharField(max_length=200)
    GrossWeight = models.FloatField()
    NetWeight = models.FloatField()
    GwNwRatio = models.FloatField()
    carton = models.IntegerField()
    quantity = models.IntegerField()
    UnitPrice = models.FloatField()
    currency = models.CharField(max_length=3)
    TotalAmount = models.FloatField()
    PackOrSet = models.CharField(max_length=200)
    UnitPriceBreakdown = models.FloatField()
    pig = models.IntegerField() #P.I.G
    CoO = models.CharField(max_length=200) #Country of Origin
    PackingMethod = models.CharField(max_length=200)
    HSCode = models.CharField(max_length=200)
    USIMno = models.IntegerField(default = 0)
    isReviewed = models.BooleanField(default= False)

    def __str__(self):
        return "Purchase order no " + self.PONumber

class supplier_details(models.Model):
    SuppCode = models.IntegerField()
    SupplierName = models.CharField(max_length=200)
    RexNo = models.CharField(max_length=10)
    SupplierAddress = models.CharField(max_length=200)

    def __str__(self):
        return "Supplier Name: " + self.SupplierName