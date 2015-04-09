from django.db import models

# Create your models here.
class Prof2Lang(models.Model):
    # the professor ID is primary key
    profID = models.IntegerField(primary_key=True)
    # professor profile
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=80)
    shortName = models.CharField(max_length=3)

    tell = models.CharField(blank=True, max_length=15)
    email = models.EmailField(blank=True)
    sahakornAccount = models.CharField(blank=True, max_length=100)

    department = models.CharField(max_length=200)
    faculty = models.CharField(max_length=200)

    def __unicode__(self):
        return self.firstName + " " + self.lastName

class Subject(models.Model):
    subjectID = models.IntegerField(primary_key=True, max_length=9)
    subjectName = models.CharField(max_length=200)

    def __unicode__(self):
        return self.subjectName

class Section(models.Model):
    sectionID = models.CharField(primary_key=True, max_length=7)
    subject = models.ForeignKey(Subject)
    classroom = models.CharField(max_length=20)
    startTime = models.TimeField()
    endTime = models.TimeField()

    dateChoices = (
        ('M', 'Monday'),
        ('T', 'Tuesday'),
        ('W', 'Wednesday'),
        ('H', 'Thursday'),
        ('F', 'Friday'),
        ('S', 'Saturday')
    )
    date = models.CharField(max_length=1, choices=dateChoices)

    def __unicode__(self):
        return self.sectionID

    class meta:
        unique_together = ('sectionID', 'subject')

class Teach(models.Model):
    prof = models.ForeignKey(Prof2Lang)
    subject = models.ForeignKey(Subject)
    section = models.ForeignKey(Section)

class HourlyEmployee(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=80)
    numberTaxpayment = models.CharField(max_length=20)
    status = models.CharField(max_length=50)
    employmentRate = models.FloatField(max_length=10, default=0.0)

    def __unicode__(self):
        return self.firstName + " " + self.lastName

class Work(models.Model):
    releaseDate = models.DateField(auto_now=True)
    startTime = models.TimeField()
    endTime = models.TimeField()
    employee = models.ForeignKey(HourlyEmployee)

    class meta:
        unique_together = ('employee', 'id')