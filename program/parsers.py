import json
from django.db import models
from program.models import mods, agency

def modimport():

    KSP_DIR = agency.objects.order_by('agency_name').first().ksp_dir
    install = open(
        KSP_DIR + '/CKAN/installed-default.ckan')
    repo = open(
        KSP_DIR + '/CKAN/registry.json')

    json_install = json.load(install)
    json_repo = json.load(repo)

    mod_list = json_install['depends']
    all_mods = json_repo['available_modules']

    for item in mod_list:
        print('managing: ' + item['name'] + ' ' + item['version'])
        modinfo = all_mods[item['name']]['module_version'][item['version']]
        item['author'] = modinfo['author'][0]
        item['desc'] = modinfo['abstract']
        item['url'] = modinfo['resources']['homepage']
        item['ksp_version'] = modinfo['ksp_version']

    print(mod_list[0])

    for mod in mod_list:
        q = mods(name=mod['name'], author=mod['author'], version=mod['version'], ksp_version=mod[
                 'ksp_version'], url=mod['url'], desc=mod['desc'], notes='')
        print(q)
        q.save()

def parsecraft():
    return('nice!')
