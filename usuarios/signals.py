from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Usuario,UsuarioEmpresa

@receiver(post_save, sender=Usuario)
def criar_vinculo_ususrio_empresa(sender, instance, created, **kwargs):
 if created:
  UsuarioEmpresa.objects.create(
   usuario=instance,
   empresa=instance.empresa
  )