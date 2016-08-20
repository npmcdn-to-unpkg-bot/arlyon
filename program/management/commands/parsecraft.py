from django.core.management.base import BaseCommand, CommandError
import json
from shutil import copyfile
from django.db import models
from program.models import agency
from django.conf import settings

class Command(BaseCommand):
    help = 'Returns important information about a ship.'

    def add_arguments(self, parser):
        parser.add_argument('ship', type=str)

    def handle(self, *args, **options):
        agencyinfo = agency.objects.first()
        ship = options['ship']

        craft = open(agencyinfo.ksp_dir+'/saves/'+agencyinfo.agency_name+'/Ships/VAB/'+ship)

        shipname = ship.rsplit( ".", 1 )[ 0 ] # the ships name
        copyfile(agencyinfo.ksp_dir+'/thumbs/'+agencyinfo.agency_name+'_VAB_'+shipname+".png", settings.BASE_DIR+'/program/static/ships/thumbs/'+shipname+'.png') # copy the thumbnail
