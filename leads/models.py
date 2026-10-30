from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")
    email = models.EmailField(verbose_name="E-mail")
    company = models.CharField(max_length=255, blank=True, null=True, verbose_name="Empresa")
    phone = models.CharField(max_length=50, blank=True, null=True, verbose_name="Telefone")
    service_interest = models.CharField(max_length=100, blank=True, null=True, verbose_name="Interesse")
    message = models.TextField(blank=True, null=True, verbose_name="Mensagem")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.email}"