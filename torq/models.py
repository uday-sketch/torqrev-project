from django.db import models

class registration(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=8)
    phone = models.IntegerField()
    address = models.CharField(max_length=200, null=True, blank=True)
    role_choice = (
        ('ADMIN', "admin"),
        ('CUSTOMER', "customer"),
        ('SELLER', "seller")
    )
    company = models.CharField(max_length=60)
    image = models.ImageField(upload_to='user/', null = True, blank = True)
    role = models.CharField(choices=role_choice, max_length=10, null=True, blank=True)

    def __str__(self):
        return self.email
    
class service_pro(models.Model):
    name = models.CharField(max_length=50)
    
class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class service_tb(models.Model):
    # Fields based on the image description
    service_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('registration', on_delete=models.CASCADE)  # Assuming 'Registration' is the related table
    service_pro_id = models.ForeignKey('service_pro', on_delete=models.CASCADE)  # Assuming 'ServicePro' is the related table
    vehicle_type = models.CharField(max_length=50)
    service_type = models.CharField(max_length=20, choices=[('regular', 'Regular'), ('emergency', 'Emergency')])
    service_desc = models.CharField(max_length=200, null=True, blank=True)
    service_date = models.DateField()
    emergency_contact = models.CharField(max_length=20, null=True, blank=True)
    service_status = models.CharField(max_length=20, choices=[('scheduled', 'Scheduled'), ('completed', 'Completed'), ('canceled', 'Canceled')])
    service_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    service_time = models.TimeField()
    pay_status = models.CharField(max_length=20, default='NOT PAID')

    def __str__(self):
        return f"Service {self.service_id} - {self.vehicle_type} - {self.service_status}"

    
