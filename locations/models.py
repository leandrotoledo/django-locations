from django.db import models
from django.utils.translation import ugettext_lazy as _

class Country(models.Model):
    name = models.CharField(_(u'Country'), max_length=255, unique=True, db_index=True)
    code = models.CharField(_(u'Code'), max_length=2, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')

class Region(models.Model):
    name = models.CharField(_(u'Region'), max_length=255, unique=True)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _('Region')
        verbose_name_plural = _('Regions')
        
class State(models.Model):
    name = models.CharField(_(u'State'), max_length=255, unique=True, db_index=True)
    code = models.CharField(_(u'Code'), max_length=2, unique=True)
    region = models.ForeignKey(Region)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _('State')
        verbose_name_plural = _('States')

class MesoRegion(models.Model):
    name = models.CharField(_(u'Mesoregion'), max_length=255, unique=True)
    state = models.ForeignKey(State)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _('mesoregion')
        verbose_name_plural = _('mesoregions')

class MicroRegion(models.Model):
    name = models.CharField(_(u'Microregion'), max_length=255)
    mesoregion =  models.ForeignKey(MesoRegion)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        unique_together = ('name', 'mesoregion')
        verbose_name = _('microregion')
        verbose_name_plural = _('microregions')
        
class Municipality(models.Model):
    name = models.CharField(_(u'Municipality'), max_length=255, db_index=True)
    microregion = models.ForeignKey(MicroRegion)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        unique_together = ('name', 'microregion')
        verbose_name = _('municipality')
        verbose_name_plural = _('municipalities')

class District(models.Model):
    name = models.CharField(_(u'District'), max_length=255)
    municipality = models.ForeignKey(Municipality)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        unique_together = ('name', 'municipality')
        verbose_name = _('district')
        verbose_name_plural = _('districts')
        
class Neighborhood(models.Model):
    name = models.CharField(_(u'Neighborhood'), max_length=255)
    district = models.ForeignKey(District)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        unique_together = ('name', 'district')
        verbose_name = _('neighborhood')
        verbose_name_plural = _('neighborhoods')
        
class Coordinate(models.Model):
    latitude = models.FloatField(_('latitude'), blank=True, null=True)
    longitude = models.FloatField(_('longitude'), blank=True, null=True)
    postal_code = models.CharField(_('postal code'), max_length=10, blank=True, null=True)
    street_name = models.CharField(_('street name'), max_length=255)
    street_number = models.CharField(_('street number'), max_length=24)
    
    class Meta:
        verbose_name = _('coordinate')
        verbose_name_plural = _('coordinates')

class Place(models.Model):
    municipality = models.ForeignKey(Municipality)
    neighborhood = models.ForeignKey(Neighborhood, blank=True, null=True)
    coordinate = models.ForeignKey(Coordinate)

    @property
    def country(self):
        return self.municipality.microregion.mesoregion.state.country

    @property
    def state(self):
        return self.municipality.microregion.mesoregion.state

    @property
    def mesoregion(self):
        return self.municipality.microregion.mesoregion

    @property
    def microregion(self):
        return self.municipality.microregion

    @property
    def latitude(self):
        return self.coordinate.latitude

    @property
    def longitude(self):
        return self.coordinate.longitude

    def __unicode__(self):
        return u'{}, {} - {}'.format(
            self.coordinate.street_name,
            self.coordinate.street_number,
            self.municipality)

    class Meta:
        verbose_name = _('Place')
        verbose_name_plural = _('Places')
