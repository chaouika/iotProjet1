from django.core.mail import send_mail
from django.db import models





class Dht11(models.Model):
   temp = models.FloatField(null=True)
   hum = models.FloatField(null=True)
   dt = models.DateTimeField(auto_now_add=True,null=True)
   def __str__(self):
      return '%s:  %s' % (self.temp, self.dt)

   def save(self, *args, **kwargs):
    if self.temp > 40:
      print(self.temp)
      from DHT.views import sendtele
      sendtele()
      send_mail('temperature depasse la normale ITIRC4,' + str(self.temp),'anomalie dans la machine,'+str(self.dt),
                   'kawtar.chaoui@ump.ac.ma',
                   ['hanae.ouarradi@ump.ac.ma'],
                    fail_silently= False,
             )
    return super().save(*args, **kwargs)




