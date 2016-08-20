from django.db import models
from django.conf import settings

# TODO:20 sort out all the model fields (especially the ones for the
# missions. they don't need to be default=0)

BASE_DIR = settings.BASE_DIR


class kerbals(models.Model):
    name = models.CharField(max_length=200)
    adddate = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    career = models.CharField(max_length=9, blank=True, null=True)
    alive = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Kerbals"


class grandStatus(models.Model):
    name = models.CharField(max_length=200)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Mission Grand Statuses"


class settings(models.Model):
    # 0 = advanced, 1 = medium, 2 = simple
    name = models.CharField(max_length=100, default='')
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Settings"


class programs(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.FilePathField(
        path=BASE_DIR + "/program/static/programs/")

    def __str__(self):
        return self.code

    class Meta:
        verbose_name_plural = "Programs"


class missionstatuses(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    color = models.CharField(max_length=6)
    grandstatus = models.ForeignKey(grandStatus, on_delete=models.SET("1"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Mission Statuses"


class shiptypes(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    color = models.CharField(max_length=6, default='000000')
    image = models.FilePathField(
        path=BASE_DIR + "/program/static/shiptypes/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Ship Types"


class mods(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=20)
    ksp_version = models.CharField(max_length=20, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    desc = models.TextField(max_length=1000, blank=True, null=True)
    notes = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Mods"


class ships(models.Model):
    name = models.CharField(max_length=200)
    shiptype = models.ForeignKey(shiptypes, on_delete=models.SET("Unknown"))
    cost = models.IntegerField(default=0)
    deltav = models.IntegerField(default=0)
    crewcapacity = models.IntegerField(default=0)
    desc = models.CharField(max_length=1000)
    parts = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Ships"


class colors(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=6)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Colors"


class agency(models.Model):
    agency_name = models.CharField(max_length=200)
    agency_flag = models.FilePathField(
        path=BASE_DIR + "/program/static/flags/")
    agency_bio = models.CharField(max_length=10000)
    agency_color = models.ForeignKey(colors, on_delete=models.SET("red"))
    time = models.IntegerField(default=0)
    ksp_dir = models.CharField(max_length=500)

    def __str__(self):
        return self.agency_name

    class Meta:
        verbose_name_plural = "Agencies"


class missions(models.Model):
    # mission details
    programid = models.ForeignKey(programs, on_delete=models.SET("Unknown"))
    missionid = models.IntegerField(default=0)
    status = models.ForeignKey(
        missionstatuses, on_delete=models.SET("Unknown"))
    # planning stage
    ship = models.ForeignKey(ships, on_delete=models.SET(
        "Unknown"), related_name='mission_ship')
    launcher = models.ForeignKey(ships, on_delete=models.SET(
        "Unknown"), related_name='mission_launcher', blank=True, null=True)
    plan = models.CharField(max_length=1000)
    # contruction
    builddate = models.IntegerField(default=0)
    fundsbefore = models.IntegerField(default=0)  # money before purchase
    cost = models.IntegerField(default=0)
    totaldeltav = models.IntegerField(default=0)
    stages = models.IntegerField(default=0)
    parts = models.IntegerField(default=0)
    mass = models.IntegerField(default=0)
    # launch
    launchdate = models.IntegerField(default=0)
    crewmembers = models.ManyToManyField('kerbals')
    # recovery
    summary = models.CharField(max_length=1000, blank=True)
    recdate = models.IntegerField(default=0)
    scichange = models.IntegerField(default=0)
    totalsci = models.IntegerField(default=0)
    fundschange = models.IntegerField(default=0)
    totalfunds = models.IntegerField(default=0)
    repchange = models.IntegerField(default=0)
    totalrep = models.IntegerField(default=0)

    def __str__(self):
        return str(self.programid) + '-' + str(self.missionid)

    class Meta:
        verbose_name_plural = "Missions"


class missionNodes(models.Model):
    nodeMission = models.ForeignKey('missions', on_delete=models.SET("None"))
    description = models.CharField(max_length=100)
    date = models.IntegerField(default=0)
    destination = models.ForeignKey('deltavMap', on_delete=models.SET("Kerbin"))

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = "Mission Nodes"

class deltavMap(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.SET("Kerbin"), null=True, blank=True)
    deltav = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Delta V Map"
