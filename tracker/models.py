from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# choices are used in the form, but not enforced at the model level
EVENT_TYPES = [(v,v) for v in (
    ('Aerial Bombardment'),
    ('Artillery Bombardment'),
    ('Attack: IED'),
    ('Attack: Mine'),
    ('Attack: Small Arms'),
    ('Attack: Mechanized'),
    ('Attack on Vehicles'),
    ('Armed Incursion'),
    ('Troop Movement'),
    ('Civilian Displacement'),
)]

EVIDENCE_SOURCES = [(v,v) for v in (
    ('Confidential Source'),
    ('Satellite Image'),
    ('NGO Report'),
    ('UN Report'),
    ('Media Report'),
    ('Government Report'),
    ('HSBA - Small Arms Survey'),
    ('SVM (Sudan Vote Monitor)'),
)]

ACTORS = [(v,v) for v in (
    ('SAF (Sudan Armed Forces)'),
    ('NGO (Non-Governmental Organization)'),
    ('SPLA/GOSS (Sudan\'s People Liberation Army/Government of South Sudan)'),
    ('UNMIS (United Nations Mission In Sudan)'),
    ('Militia - Specify militia'),
    ('PDF (Popular Defense Force)'),
)]

class Event(models.Model):
    summary = models.CharField(max_length=255, verbose_name="Summary", help_text="Short summary of event (one phrase or sentence)")
    type = models.CharField(max_length=255, choices=EVENT_TYPES, verbose_name="Event Type")
    date = models.DateField(verbose_name="Event Date", help_text="Date on which the event occurred")
    location = models.CharField(max_length=255, verbose_name="Location", help_text="Where the event occurred")
    lat = models.FloatField(blank=True, verbose_name="Latitude")
    lon = models.FloatField(blank=True, verbose_name="Longitude")
    actor = models.CharField(max_length=255, choices=ACTORS, help_text="The group or persons responsible for the event")
    population = models.CharField(max_length=255, verbose_name="Affected Population", 
        help_text='Specify "Internally Displaced Persons", "Residents of [Town]", a particular military unit, etc')
    notes = models.TextField(blank=True, verbose_name="Notes")
    logger = models.ForeignKey(User)
    
    class Meta:
        ordering = ['-date']
        
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('event_view', kwargs={"id": self.id})

class Evidence(models.Model):
    summary = models.CharField(max_length=255, verbose_name="Summary", help_text="Short summary of evidence (one phrase or sentence)")
    event = models.ForeignKey(Event, verbose_name="Related Event", help_text="The event to which this evidence is related, if known")
    source = models.CharField(max_length=255, choices=EVIDENCE_SOURCES, verbose_name="Source")
    confidential_id = models.CharField(max_length=255, verbose_name="Confidential Source ID")
    confidential_link = models.CharField(max_length=255, verbose_name="Confidential Source Link/File Number")
    source_link = models.CharField(max_length=255, verbose_name="Source Link", help_text="URL of source report or image")
    # do we need a file upload option here?
    notes = models.TextField(blank=True, verbose_name="Notes")
    logger = models.ForeignKey(User)
    