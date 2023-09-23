from django.db import models

class customer(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    # ...
class vendor(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    # ...
class forWardingAgents(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    # ...
class shipper(models.Model):
    customers = models.ManyToManyField(customer, blank=True, related_name='shippers')
    vendors = models.ManyToManyField(vendor, blank=True, related_name='shippers')
    agents = models.ManyToManyField(forWardingAgents, blank=True, related_name='shippers')
    # ...
class issuedBy(models.Model):
    forWardingAgents = models.ForeignKey(forWardingAgents, blank=True, on_delete=models.DO_NOTHING)
    wareHouseProvider = models.ForeignKey(wareHouseProviders, blank=True, on_delete=models.DO_NOTHING)
    # ...
class pickUpLocation(models.Model):
    customers = models.ManyToManyField(customer, blank=True, related_name='shippersa')
    vendors = models.ManyToManyField(vendor, blank=True, related_name='shippersb')
    agents = models.ManyToManyField(forWardingAgents, blank=True, related_name='shippersc')
    # ...
class consignee(models.Model):
    customers = models.ManyToManyField(customer, blank=True, related_name='shipp')
    vendors = models.ManyToManyField(vendor, blank=True, related_name='shi')
    agents = models.ManyToManyField(forWardingAgents, blank=True, related_name='sh')
    carrierName = models.ForeignKey(carrier, blank=True, null=True, on_delete=models.CASCADE, related_name='sss')
    # ...
class deliveryLocation(models.Model):
    customers = models.ManyToManyField(customer, blank=True, related_name='ship')
    vendors = models.ManyToManyField(vendor, blank=True, related_name='ship')
    agents = models.ManyToManyField(forWardingAgents, blank=True, related_name='ship')
    carrierName = models.ForeignKey(carrier, blank=True, null=True, on_delete=models.CASCADE, related_name='ship')
    # ...
class pickUpOrder(models.Model):
    status = models.CharField(max_length=200, blank=True, null=True)
    number = models.PositiveBigIntegerField(blank=True, null=True)
    creationDate = models.DateField(blank=True, null=True)
    pickUpDate = models.DateField(blank=True, null=True)
    deliveryDate = models.DateField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    issuedByKey = models.ForeignKey(forWardingAgents, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='issuedBy')
    destinationAgentKey = models.ForeignKey(forWardingAgents, blank=True, null=True, on_delete=models.DO_NOTHING)
    employeekey = models.ForeignKey(employee, blank=True, null=True, on_delete=models.DO_NOTHING)
    shipperkey = models.ForeignKey(customer, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='shipper')
    PickUpLocationkey = models.ForeignKey(customer, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='pickUpLocation')
    consigneekey = models.ForeignKey(customer, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='consigneekey')
    deliveryLocationkey = models.ForeignKey(customer, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='deliveryLocation')
    inlandCarrierKey = models.ForeignKey(carrier, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='inlandCarri')
    mainCarrierKey = models.ForeignKey(carrier, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='mainCarri')
    proNumber = models.CharField(max_length=200, blank=True, null=True)
    trackingNumber = models.CharField(max_length=200, blank=True, null=True)
    supplierKey = models.ForeignKey(customer, blank=True, null=True, on_delete=models.DO_NOTHING)
    invoiceNumber = models.CharField(max_length=200, blank=True, null=True)
    purchaseOrderNum = models.CharField(max_length=200, blank=True, null=True)
    # ...

class pieces(models.Model):
    status = models.FloatField(blank=True, null=True, default=0)
    package = models.FloatField(blank=True, null=True, default=0)
    description = models.FloatField(blank=True, null=True, default=0)
    pieces = models.FloatField(blank=True, null=True, default=0)
    length = models.FloatField(blank=True, null=True, default=0)
    height = models.FloatField(blank=True, null=True, default=0)
    width = models.FloatField(blank=True, null=True, default=0)
    weight = models.FloatField(blank=True, null=True, default=0)
    volume = models.FloatField(blank=True, null=True, default=0)


