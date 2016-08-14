from flipper.models import item
from django.core.management.base import BaseCommand, CommandError
import json
from urllib.request import urlopen
import urllib.parse
from time import sleep


class Command(BaseCommand):
    help = 'Populates the item list with data from the GE.'

    def handle(self, *args, **options):

        itemobject = [
            {
                "name": "Abyssal whip",
                "number": 10
            },
            {
                "name": "Adamant axe",
                "number": 40
            },
            {
                "name": "Adamant arrow",
                "number": 11000
            },
            {
                "name": "Adamant dart",
                "number": 11000
            },
            {
                "name": "Adamant dart tip",
                "number": 11000
            },
            {
                "name": "Adamant full helm",
                "number": 125
            },
            {
                "name": "Adamant javelin",
                "number": 11000
            },
            {
                "name": "Adamant pickaxe",
                "number": 40
            },
            {
                "name": "Adamant platebody",
                "number": 125
            },
            {
                "name": "Adamantite bar",
                "number": 10000
            },
            {
                "name": "Adamantite ore",
                "number": 4500
            },
            {
                "name": "Air battlestaff",
                "number": 14000
            },
            {
                "name": "Air orb",
                "number": 10000
            },
            {
                "name": "Air rune",
                "number": 20000
            },
            {
                "name": "Amulet of fury",
                "number": 8
            },
            {
                "name": "Amulet of power",
                "number": 125
            },
            {
                "name": "Amulet of strength",
                "number": 125
            },
            {
                "name": "Amulet of glory",
                "number": 10000
            },
            {
                "name": "Archers ring",
                "number": 8
            },
            {
                "name": "Archery ticket",
                "number": 14000
            },
            {
                "name": "Armadyl chainskirt",
                "number": 8
            },
            {
                "name": "Armadyl chestplate",
                "number": 8
            },
            {
                "name": "Armadyl helmet",
                "number": 10
            },
            {
                "name": "Arrows",
                "number": 7000
            },
            {
                "name": "Arrow shaft",
                "number": 7000
            },
            {
                "name": "Astral rune",
                "number": 10000
            },
            {
                "name": "Bandos boots",
                "number": 8
            },
            {
                "name": "Bandos chestplate",
                "number": 8
            },
            {
                "name": "Bandos godsword",
                "number": 8
            },
            {
                "name": "Bandos tassets",
                "number": 8
            },
            {
                "name": "Barrows equipment",
                "number": "10 (or 15)"
            },
            {
                "name": "Battlestaff",
                "number": 11000
            },
            {
                "name": "Berserker helm",
                "number": 70
            },
            {
                "name": "Berserker ring",
                "number": 8
            },
            {
                "name": "Big bones",
                "number": 3000
            },
            {
                "name": "Bird snare",
                "number": 250
            },
            {
                "name": "Black axe",
                "number": 40
            },
            {
                "name": "Black chinchompa",
                "number": 6000
            },
            {
                "name": "Black d'hide body",
                "number": 70
            },
            {
                "name": "Black d'hide chaps",
                "number": 70
            },
            {
                "name": "Black dragonhide",
                "number": 10000
            },
            {
                "name": "Black pickaxe",
                "number": 40
            },
            {
                "name": "Blood rune",
                "number": 10000
            },
            {
                "name": "Blue d'hide body",
                "number": 125
            },
            {
                "name": "Blue dragonhide",
                "number": 13000
            },
            {
                "name": "Body rune",
                "number": 12000
            },
            {
                "name": "Bolt rack",
                "number": 11000
            },
            {
                "name": "Bones",
                "number": 3000
            },
            {
                "name": "Bow string",
                "number": 13000
            },
            {
                "name": "Bows",
                "number": 125
            },
            {
                "name": "Box trap",
                "number": 250
            },
            {
                "name": "Brine sabre",
                "number": 8
            },
            {
                "name": "Broad bolts",
                "number": 7000
            },
            {
                "name": "Bronze axe",
                "number": 40
            },
            {
                "name": "Bronze dart",
                "number": 7000
            },
            {
                "name": "Bronze pickaxe",
                "number": 40
            },
            {
                "name": "Bucket of sand",
                "number": 13000
            },
            {
                "name": "Cannonball",
                "number": 7000
            },
            {
                "name": "Chaos rune",
                "number": 12000
            },
            {
                "name": "Chinchompa",
                "number": 7000
            },
            {
                "name": "Chef's hat",
                "number": 150
            },
            {
                "name": "Chocolate bar",
                "number": 13000
            },
            {
                "name": "Chocolate dust",
                "number": 13000
            },
            {
                "name": "Christmas cracker",
                "number": 50
            },
            {
                "name": "Clay",
                "number": 13000
            },
            {
                "name": "Climbing boots",
                "number": 15
            },
            {
                "name": "Coal",
                "number": 13000
            },
            {
                "name": "Coif",
                "number": 125
            },
            {
                "name": "Compost",
                "number": 600
            },
            {
                "name": "Compost potion(1)",
                "number": 50
            },
            {
                "name": "Compost potion(2)",
                "number": 50
            },
            {
                "name": "Compost potion(3)",
                "number": 50
            },
            {
                "name": "Compost potion(4)",
                "number": 50
            },
            {
                "name": "Copper ore",
                "number": 13000
            },
            {
                "name": "Cosmic rune",
                "number": 12000
            },
            {
                "name": "Cowhide",
                "number": 10000
            },
            {
                "name": "Dark bow",
                "number": 8
            },
            {
                "name": "Dart tips",
                "number": 10000
            },
            {
                "name": "Death rune",
                "number": 10000
            },
            {
                "name": "Dharok's armour set",
                "number": 8
            },
            {
                "name": "Disk of returning",
                "number": 5
            },
            {
                "name": "Dragon axe",
                "number": 40
            },
            {
                "name": "Dragon arrow",
                "number": 11000
            },
            {
                "name": "Dragon battleaxe",
                "number": 70
            },
            {
                "name": "Dragon boots",
                "number": 70
            },
            {
                "name": "Dragon bones",
                "number": 7500
            },
            {
                "name": "Dragon dagger",
                "number": 70
            },
            {
                "name": "Dragon longsword",
                "number": 70
            },
            {
                "name": "Dragon mace",
                "number": 70
            },
            {
                "name": "Dragon pickaxe",
                "number": 40
            },
            {
                "name": "Dragon scimitar",
                "number": 70
            },
            {
                "name": "Dragonfire shield",
                "number": 10
            },
            {
                "name": "Dust rune",
                "number": 12000
            },
            {
                "name": "Earth battlestaff",
                "number": 500
            },
            {
                "name": "Earth rune",
                "number": 20000
            },
            {
                "name": "Energy potion(1)",
                "number": 2000
            },
            {
                "name": "Energy potion(2)",
                "number": 2000
            },
            {
                "name": "Energy potion(3)",
                "number": 2000
            },
            {
                "name": "Energy potion(4)",
                "number": 2000
            },
            {
                "name": "Feather",
                "number": 13000
            },
            {
                "name": "Fire battlestaff",
                "number": 500
            },
            {
                "name": "Fire rune",
                "number": 20000
            },
            {
                "name": "Fishing bait",
                "number": 8000
            },
            {
                "name": "Flax",
                "number": 13000
            },
            {
                "name": "Flowers",
                "number": 250
            },
            {
                "name": "Frozen whip mix",
                "number": 4
            },
            {
                "name": "Fury ornament kit",
                "number": 4
            },
            {
                "name": "Goblin mail",
                "number": 15
            },
            {
                "name": "Gold amulet (u)",
                "number": 18000
            },
            {
                "name": "Gold bar",
                "number": 10000
            },
            {
                "name": "Gold ore",
                "number": 13000
            },
            {
                "name": "Granite maul",
                "number": 70
            },
            {
                "name": "Grapes",
                "number": 13000
            },
            {
                "name": "Green d'hide body",
                "number": 125
            },
            {
                "name": "Green d'hide chaps",
                "number": 125
            },
            {
                "name": "Green d'hide vamb",
                "number": 125
            },
            {
                "name": "Green dragonhide",
                "number": 13000
            },
            {
                "name": "Hammer",
                "number": 40
            },
            {
                "name": "Hard leather",
                "number": 10000
            },
            {
                "name": "Helm of neitiznot",
                "number": 70
            },
            {
                "name": "High level herbs",
                "number": 2000
            },
            {
                "name": "Holy elixir",
                "number": 4
            },
            {
                "name": "Infinity boots",
                "number": 24
            },
            {
                "name": "Infinity hat",
                "number": 10
            },
            {
                "name": "Inoculation bracelet",
                "number": 505
            },
            {
                "name": "Iron arrow",
                "number": 7000
            },
            {
                "name": "Iron axe",
                "number": 40
            },
            {
                "name": "Iron bar",
                "number": 10000
            },
            {
                "name": "Iron dart",
                "number": 7000
            },
            {
                "name": "Iron knife",
                "number": 7000
            },
            {
                "name": "Iron ore",
                "number": 13000
            },
            {
                "name": "Iron pickaxe",
                "number": 40
            },
            {
                "name": "Iron platebody",
                "number": 125
            },
            {
                "name": "Jug of water",
                "number": 13000
            },
            {
                "name": "Jug of wine",
                "number": 6000
            },
            {
                "name": "Kraken tentacle",
                "number": 10
            },
            {
                "name": "Lava battlestaff",
                "number": 8
            },
            {
                "name": "Lava rune",
                "number": 12000
            },
            {
                "name": "Law rune",
                "number": 12000
            },
            {
                "name": "Leather",
                "number": 10000
            },
            {
                "name": "Leather body",
                "number": 125
            },
            {
                "name": "Leather chaps",
                "number": 125
            },
            {
                "name": "Leather gloves",
                "number": 125
            },
            {
                "name": "Limpwurt seed",
                "number": 600
            },
            {
                "name": "Lobster",
                "number": 6000
            },
            {
                "name": "Logs",
                "number": 14000
            },
            {
                "name": "Longbow",
                "number": 14000
            },
            {
                "name": "Loop half of key",
                "number": 11000
            },
            {
                "name": "Low level herbs",
                "number": 12000
            },
            {
                "name": "Magic fang",
                "number": 5
            },
            {
                "name": "Magic logs",
                "number": 12000
            },
            {
                "name": "Magic longbow",
                "number": 18000
            },
            {
                "name": "Magic longbow (u)",
                "number": 10000
            },
            {
                "name": "Maple logs",
                "number": 15000
            },
            {
                "name": "Maple longbow",
                "number": 14000
            },
            {
                "name": "Magic seed",
                "number": 200
            },
            {
                "name": "Maple shortbow (u)",
                "number": 10000
            },
            {
                "name": "Mahogany logs",
                "number": 11000
            },
            {
                "name": "Mind rune",
                "number": 12000
            },
            {
                "name": "Mist rune",
                "number": 12000
            },
            {
                "name": "Mithril arrow",
                "number": 7000
            },
            {
                "name": "Mithril axe",
                "number": 40
            },
            {
                "name": "Mithril bar",
                "number": 10000
            },
            {
                "name": "Mithril dart",
                "number": 7000
            },
            {
                "name": "Mithril ore",
                "number": 13000
            },
            {
                "name": "Mithril pickaxe",
                "number": 40
            },
            {
                "name": "Mithril platebody",
                "number": 125
            },
            {
                "name": "Mole claw",
                "number": 50
            },
            {
                "name": "Mole skin",
                "number": 50
            },
            {
                "name": "Molten glass",
                "number": 13000
            },
            {
                "name": "Monkfish",
                "number": 13000
            },
            {
                "name": "Monk's robe",
                "number": 125
            },
            {
                "name": "Monk's robe top",
                "number": 125
            },
            {
                "name": "Mud rune",
                "number": 12000
            },
            {
                "name": "Nature rune",
                "number": 12000
            },
            {
                "name": "Oak logs",
                "number": 14000
            },
            {
                "name": "Oak longbow",
                "number": 14000
            },
            {
                "name": "Occult necklace",
                "number": 8
            },
            {
                "name": "Palm tree seed",
                "number": 200
            },
            {
                "name": "Papaya tree seed",
                "number": 200
            },
            {
                "name": "Partyhats",
                "number": 5
            },
            {
                "name": "Pegasian crystal",
                "number": 15
            },
            {
                "name": "Pie dish",
                "number": 500
            },
            {
                "name": "Plank",
                "number": 13000
            },
            {
                "name": "Prayer potion(1)",
                "number": 2000
            },
            {
                "name": "Prayer potion(2)",
                "number": 2000
            },
            {
                "name": "Prayer potion(3)",
                "number": 2000
            },
            {
                "name": "Prayer potion(4)",
                "number": 2000
            },
            {
                "name": "Pure essence",
                "number": 20000
            },
            {
                "name": "Ranarr seed",
                "number": 200
            },
            {
                "name": "Ranger boots",
                "number": 6
            },
            {
                "name": "Rares",
                "number": 50
            },
            {
                "name": "Raw beef",
                "number": 13000
            },
            {
                "name": "Raw shark",
                "number": 15000
            },
            {
                "name": "Red chinchompa",
                "number": 7000
            },
            {
                "name": "Red dragonhide",
                "number": 10000
            },
            {
                "name": "Regen bracelet",
                "number": 10
            },
            {
                "name": "Rune armour",
                "number": 70
            },
            {
                "name": "Rune armour set (lg)/Rune armour set (sk)",
                "number": 8
            },
            {
                "name": "Rune arrow",
                "number": 11000
            },
            {
                "name": "Rune axe",
                "number": 40
            },
            {
                "name": "Runite bolts",
                "number": 10000
            },
            {
                "name": "Runite ore",
                "number": 4500
            },
            {
                "name": "Rune dart",
                "number": 7000
            },
            {
                "name": "Rune kiteshield (g)",
                "number": 8
            },
            {
                "name": "Rune pickaxe",
                "number": 40
            },
            {
                "name": "Rune weapons",
                "number": 70
            },
            {
                "name": "Rope",
                "number": 250
            },
            {
                "name": "Saradomin brew(1)",
                "number": 2000
            },
            {
                "name": "Saradomin brew(2)",
                "number": 2000
            },
            {
                "name": "Saradomin brew(3)",
                "number": 2000
            },
            {
                "name": "Saradomin brew(4)",
                "number": 2000
            },
            {
                "name": "Saradomin sword",
                "number": 8
            },
            {
                "name": "Santa hat",
                "number": 5
            },
            {
                "name": "Sapphire",
                "number": 3000
            },
            {
                "name": "Seercull",
                "number": 8
            },
            {
                "name": "Seers ring",
                "number": 8
            },
            {
                "name": "Serpentine helm (uncharged)",
                "number": 5
            },
            {
                "name": "Serpentine visage",
                "number": 5
            },
            {
                "name": "Shark",
                "number": 10000
            },
            {
                "name": "Shrimps",
                "number": 15000
            },
            {
                "name": "Silk",
                "number": 18000
            },
            {
                "name": "Silver sickle",
                "number": 15
            },
            {
                "name": "Smoke rune",
                "number": 12000
            },
            {
                "name": "Soda ash",
                "number": 13000
            },
            {
                "name": "Soul rune",
                "number": 10000
            },
            {
                "name": "Spectral spirit shield",
                "number": 8
            },
            {
                "name": "Spirit shield",
                "number": 8
            },
            {
                "name": "Spotted cape",
                "number": 125
            },
            {
                "name": "Splitbark body",
                "number": 70
            },
            {
                "name": "Stamina potion(1)",
                "number": 2000
            },
            {
                "name": "Stamina potion(2)",
                "number": 2000
            },
            {
                "name": "Stamina potion(3)",
                "number": 2000
            },
            {
                "name": "Stamina potion(4)",
                "number": 2000
            },
            {
                "name": "Steam rune",
                "number": 12000
            },
            {
                "name": "Steel arrow",
                "number": 7000
            },
            {
                "name": "Steel axe",
                "number": 40
            },
            {
                "name": "Steel bar",
                "number": 10000
            },
            {
                "name": "Steel dart",
                "number": 7000
            },
            {
                "name": "Steel pickaxe",
                "number": 40
            },
            {
                "name": "Super attack(1)",
                "number": 2000
            },
            {
                "name": "Super defence(1)",
                "number": 2000
            },
            {
                "name": "Super restore(1)",
                "number": 2000
            },
            {
                "name": "Super strength(1)",
                "number": 2000
            },
            {
                "name": "Super attack(2)",
                "number": 2000
            },
            {
                "name": "Super defence(2)",
                "number": 2000
            },
            {
                "name": "Super restore(2)",
                "number": 2000
            },
            {
                "name": "Super strength(2)",
                "number": 2000
            },
            {
                "name": "Super attack(3)",
                "number": 2000
            },
            {
                "name": "Super defence(3)",
                "number": 2000
            },
            {
                "name": "Super restore(3)",
                "number": 2000
            },
            {
                "name": "Super strength(3)",
                "number": 2000
            },
            {
                "name": "Super attack(4)",
                "number": 2000
            },
            {
                "name": "Super defence(4)",
                "number": 2000
            },
            {
                "name": "Super restore(4)",
                "number": 2000
            },
            {
                "name": "Super strength(4)",
                "number": 2000
            },
            {
                "name": "Supercompost",
                "number": 600
            },
            {
                "name": "Swamp tar",
                "number": 13000
            },
            {
                "name": "Swordfish",
                "number": 6000
            },
            {
                "name": "Tanzanite fang",
                "number": 5
            },
            {
                "name": "Team cape",
                "number": 150
            },
            {
                "name": "Tin ore",
                "number": 13000
            },
            {
                "name": "Toxic blowpipe (empty)",
                "number": 8
            },
            {
                "name": "Trading sticks",
                "number": 18000
            },
            {
                "name": "Tuna",
                "number": 6000
            },
            {
                "name": "Unpowered orb",
                "number": 10000
            },
            {
                "name": "Varrock teleport",
                "number": 1000
            },
            {
                "name": "Vial of water",
                "number": 13000
            },
            {
                "name": "Volcanic whip mix",
                "number": 6
            },
            {
                "name": "Warrior ring",
                "number": 8
            },
            {
                "name": "Water battlestaff",
                "number": 500
            },
            {
                "name": "Watermelon seed",
                "number": 200
            },
            {
                "name": "Water rune",
                "number": 20000
            },
            {
                "name": "Willow longbow",
                "number": 14000
            },
            {
                "name": "Wine of zamorak",
                "number": 10000
            },
            {
                "name": "Yew logs",
                "number": 12000
            },
            {
                "name": "Yew longbow",
                "number": 18000
            },
            {
                "name": "Yew longbow (u)",
                "number": 10000
            },
            {
                "name": "Zamorak robe",
                "number": 15
            },
            {
                "name": "Zul-andra teleport",
                "number": 10000
            },
            {
                "name": "Zulrah's scales",
                "number": 30000
            },
            {
                "name": "Adamant platelegs",
                "number": 125
            }
        ]

        toadd = [
            {'name': 'Arrows', 'number': 7000},
            {'name': 'Barrows equipment', 'number': '10 (or 15)'},
            {'name': 'Bows', 'number': 125},
            {'name': 'Dart tips', 'number': 10000},
            {'name': 'Flowers', 'number': 250},
            {'name': 'High level herbs', 'number': 2000},
            {'name': 'Low level herbs', 'number': 12000},
            {'name': 'Partyhats', 'number': 5},
            {'name': 'Rares', 'number': 50},
            {'name': 'Rune armour', 'number': 70},
            {'name': 'Rune armour set (lg)/Rune armour set (sk)', 'number': 8},
            {'name': 'Rune weapons', 'number': 70},
            {'name': 'Team cape', 'number': 150}
        ]

        for obj in itemobject:
            entry = item.objects.filter(name=obj['name'])
            for fdsafhjk in entry:
                fdsafhjk.buylimit = obj["number"]
                fdsafhjk.save()

        print(toadd)
        print("complete!")
