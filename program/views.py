from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core import serializers
from .models import agency, kerbals, programs, missionstatuses, shiptypes, mods, ships, missions, colors
from program.parsers import modimport
import os

# TODO:0 figure out how this fucking settings.base_dir works

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def index(request):
    if request.user.is_authenticated():
        agencyinfo = agency.objects.order_by('agency_name').first()
        print(agencyinfo)
        if agencyinfo is None:
            return HttpResponseRedirect("setup/")
        return HttpResponseRedirect("missions/")
    else:
        template = loader.get_template('landing.html')
        context = {
        }
        return HttpResponse(template.render(context, request))


def importmods(request):
    modimport()
    return HttpResponseRedirect("agency/")


def setup(request):
    template = loader.get_template('setup.html')
    colorlist = colors.objects.order_by('name')
    flagdir = BASE_DIR + '/program/static/flags/'
    agencyinfo = agency.objects.order_by('agency_name').first()
    flaglist = os.listdir(flagdir)
    context = {
        'agencyinfo': agencyinfo,
        'colors': colorlist,
        'flags': flaglist,
    }
    return HttpResponse(template.render(context, request))


def kerballist(request):
    agencyinfo = agency.objects.order_by('agency_name').first()
    kerbalslist = kerbals.objects.order_by('name')
    template = loader.get_template('kerbals.html')
    context = {
        'agencyinfo': agencyinfo,
        'kerbalslist': kerbalslist,
    }
    return HttpResponse(template.render(context, request))


def programlist(request):
    agencyinfo = agency.objects.order_by('agency_name').first()
    programslist = programs.objects.order_by('name')
    template = loader.get_template('programs.html')
    context = {
        'agencyinfo': agencyinfo,
        'programslist': programslist,
    }
    return HttpResponse(template.render(context, request))


def modlist(request):
    agencyinfo = agency.objects.order_by('agency_name').first()
    modlist = mods.objects.order_by('name')
    template = loader.get_template('mods.html')
    context = {
        'agencyinfo': agencyinfo,
        'modlist': modlist,
    }
    return HttpResponse(template.render(context, request))


def modinfo(request, mod_id):
    agencyinfo = agency.objects.order_by('agency_name').first()
    modid = get_object_or_404(mods, id=mod_id)
    template = loader.get_template('modinfo.html')
    context = {
        'agencyinfo': agencyinfo,
        'mod': modid,
    }
    return HttpResponse(template.render(context, request))


def agencypage(request):
    json_serializer = serializers.get_serializer("json")()
    agencyinfo = agency.objects.order_by('agency_name').first()
    missionlist = missions.objects.order_by('programid', 'missionid')
    '''shiplist = ships.objects.order_by('name') [currently unused]'''
    ship_types = shiptypes.objects.order_by('name')
    template = loader.get_template('agency.html')
    mission_statuses = missionstatuses.objects.order_by('name')
    missionlist_json = json_serializer.serialize(
        missions.objects.all().order_by('id'))
    mission_statuses_json = json_serializer.serialize(
        missionstatuses.objects.all().order_by('id'))
    shipslist_json = json_serializer.serialize(
        ships.objects.all().order_by('id'))
    shiptypes_json = json_serializer.serialize(
        shiptypes.objects.all().order_by('id'))
    context = {
        'agencyinfo': agencyinfo,
        'missionlist': missionlist,
        'shiptypes': ship_types,
        'missionstatuses': mission_statuses,
        'missionlist_json': missionlist_json,
        'mission_statuses_json': mission_statuses_json,
        'shipslist_json': shipslist_json,
        'shiptypes_json': shiptypes_json,
    }
    return HttpResponse(template.render(context, request))


def shiplist(request):
    agency_info = agency.objects.order_by('agency_name').first()
    ship_types = shiptypes.objects.order_by('name')
    ship_list = ships.objects.order_by('shiptype', 'name')
    template = loader.get_template('ships.html')
    context = {
        'agencyinfo': agency_info,
        'shipslist': ship_list,
        'shiptypes': ship_types,
    }
    return HttpResponse(template.render(context, request))


def shipinfo(request, ship_id):
    agencyinfo = agency.objects.order_by('agency_name').first()
    shipid = get_object_or_404(ships, id=ship_id)
    shiptypes_list = shiptypes.objects.order_by('code')
    template = loader.get_template('shipinfo.html')
    context = {
        'shiptypes': shiptypes_list,
        'agencyinfo': agencyinfo,
        'ship': shipid,
    }
    return HttpResponse(template.render(context, request))


def missionlist(request):
    agency_info = agency.objects.order_by('agency_name').first()
    mission_statuses = missionstatuses.objects.order_by('name')
    missions_list = missions.objects.order_by('programid')
    programslist = programs.objects.order_by('code')
    template = loader.get_template('missions.html')
    context = {
        'agencyinfo': agency_info,
        'programs': programslist,
        'missions': missions_list,
        'missionstatuses': mission_statuses,
    }
    return HttpResponse(template.render(context, request))


def missioninfo(request, mission_id):
    agencyinfo = agency.objects.order_by('agency_name').first()
    missionid = get_object_or_404(missions, id=mission_id)
    programs_list = programs.objects.order_by('code')
    template = loader.get_template('missioninfo.html')
    crew_list = ', '.join([str(i) for i in missionid.crewmembers.all()])
    print(crew_list)
    context = {
        'programs': programs_list,
        'agencyinfo': agencyinfo,
        'mission': missionid,
        'crewlist': crew_list,
    }
    return HttpResponse(template.render(context, request))


def missionnew(request):
    programid = programs.objects.get(pk=request.POST['program'])
    ship = ships.objects.get(pk=request.POST['ship1'])
    launcher = request.POST['ship2']
    if launcher == '':
        launcher = None
    else:
        launcher = ships.objects.get(pk=launcher)
    status = missionstatuses.objects.get(pk=1)
    plan = request.POST['desc']
    missionid = missions.objects.filter(
        programid=programid).order_by('missionid')
    if missionid.last() is None:
        missionid = 1
    else:
        missionid = missionid.last().missionid + 1
    newmission = missions(programid=programid, missionid=missionid,
                          status=status, ship=ship, launcher=launcher, plan=plan)
    newmission.save()
    return HttpResponseRedirect("/missions/" + str(newmission.id))


def setupcomplete(request):
    name = str(request.POST['name'])
    color = colors.objects.get(value=request.POST['color']).id
    color = colors.objects.get(pk=color)
    flag = "flags/"+request.POST['flag']
    bio = str(request.POST['agency_bio'])
    kspdir = str(request.POST['ksp_dir'])
    agencysave = agency(pk=1, agency_name=name, agency_flag=flag,
                        agency_bio=bio, agency_color=color, ksp_dir=kspdir,)
    agencysave.save()
    return HttpResponseRedirect("/agency/")


def new(request):
    template = loader.get_template('new.html')
    agency_info = agency.objects.order_by('agency_name').first()
    ship_types = shiptypes.objects.order_by('name')
    ship_list = ships.objects.order_by('shiptype', 'name')
    mission_statuses = missionstatuses.objects.order_by('name')
    programs_list = programs.objects.order_by('code')
    launchers = ships.objects.filter(shiptype=1)
    path = BASE_DIR + "/program/static/programs/"
    program_logos = {}
    for image in os.listdir(path):
        program_logos.update({image: "programs/" + image})
    craftfiles = ()
    print(craftfiles)

    context = {
        'agencyinfo': agency_info,
        'ships': ship_list,
        'missionstatuses': mission_statuses,
        'programs': programs_list,
        'shiptypes': ship_types,
        'program_logos': program_logos,
        'launchers': launchers,
    }

    return HttpResponse(template.render(context, request))


def settingspage(request):
    template = loader.get_template('settings.html')
    agency_info = agency.objects.order_by('agency_name').first()
    context = {
        'agencyinfo': agency_info,
    }
    return HttpResponse(template.render(context, request))
