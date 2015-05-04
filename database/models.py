from django.db import models


class ResourceNode(models.Model):
    node_name = models.CharField(max_length=200)
    node_image = models.ImageField(upload_to='database', default=None, blank=True, null=True)
    node_yield = models.FloatField()
    node_respawn_time = models.IntegerField()
    node_location = models.TextField()

    def __str__(self):
        return unicode(self.node_name)


class Resource(models.Model):
    resource_node = models.ForeignKey(ResourceNode, related_name='resource')
    resource_image = models.ImageField()
    resource_name = models.CharField(max_length=200)

    def __str__(self):
        return unicode(self.resource_name)


