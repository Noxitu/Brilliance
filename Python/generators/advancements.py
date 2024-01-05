import data
from save import save
from copy import deepcopy


IMPOSSIBLE = {"auto": {"trigger": "minecraft:impossible"}}


def _create(advancement_id, advancement):
    hidden = deepcopy(advancement)
    visible = deepcopy(advancement)

    if advancement_id.endswith('/root'):
        del hidden["display"]

    visible["criteria"] = IMPOSSIBLE

    if "criteria" not in hidden:
        hidden["criteria"] = IMPOSSIBLE

    if "display" in visible:
        visible["display"].update({
        "show_toast": False,
        "announce_to_chat": False,
        "hidden": False
    })
        
    if "parent" in advancement:
        hidden["parent"] = f"do2:hidden/{advancement['parent']}"
        visible["parent"] = f"do2:visible/{advancement['parent']}"

    if "rewards" in visible:
        del visible["rewards"]

    save(f"data/do2/advancements/hidden/{advancement_id}.json", hidden)
    save(f"data/do2/advancements/visible/{advancement_id}.json", visible)


def _egg(egg_id, parent):
    model_id = data.MODELS[egg_id]
    name = data.NAMES[egg_id]
    location = data.LOCATIONS[egg_id]

    criteria = {
        "auto": {
            "trigger": "minecraft:location",
            "conditions": {
                "player": {}
            },
        }
    }

    if "area" in location:
        x_min, y_min, z_min, x_max, y_max, z_max = map(float, location["area"].split())

        criteria["auto"]["conditions"]["player"]["location"] = {
            "dimension": "minecraft:overworld",
            "position": {
                "x": {"min": x_min, "max": x_max},
                "y": {"min": y_min, "max": y_max},
                "z": {"min": z_min, "max": z_max},
            },
        }

    if True: # "egg" in location:
        criteria["auto"]["conditions"]["player"]["type_specific"] = {
            "type": "player",
            "looking_at": {
                "nbt": f"{{Tags:[\"do2.egg_hunt.is_{egg_id}_hitbox\"]}}",
                "distance": {
                    "absolute": {
                        "min": 0,
                        "max": 10,
                    }
                }
            }
        }

    _create(f"egg_hunt/eggs/{egg_id}", {
        "display": {
            "icon": {
                "item": "minecraft:carved_pumpkin",
                "nbt": f"{{'CustomModelData': {model_id}}}"
            },
            "title": name,
            "description": f"Find {name} hidden in Decked Out 2.",
            "frame": "goal",
            "show_toast": True,
            "announce_to_chat": True,
        },
        "parent": parent,
        "criteria": criteria,
        "rewards": {
            "function": f"do2:egg_hunt/rewards/{egg_id}"
        },
    })


def advancements():
    _create("egg_hunt/root", {
        "display": {
            "icon": {
                "item": "minecraft:carved_pumpkin",
                "nbt": "{'CustomModelData': 42}"
            },
            "title": "Decked Out 2 Egg Hunt",
            "description": "Find any Hermit egg hidden in Decked Out 2.",
            "background":"minecraft:textures/block/stripped_warped_stem.png",
            "frame": "task",
        }
    })

    _create("egg_hunt/egg_hunter", {
        "display": {
            "icon": {
                "item": "minecraft:carved_pumpkin",
                "nbt": "{'CustomModelData': 42}"
                # TODO: Add bunny or another icon.
            },
            "title": "Egg Hunter",
            "description": "Find all 20 Hermit eggs hidden in Decked Out 2.",
            "frame": "challenge",
            "show_toast": True,
            "announce_to_chat": True,
            # "hidden": True,
        },
        "parent": "egg_hunt/root"
    })

    # _create("egg_hunt/dlc_egg_hunter", {})

    parent = None

    for i, egg_id in enumerate(data.NAMES):
        if i % 5 == 0:
            parent = "egg_hunt/egg_hunter"
        
        _egg(egg_id, parent)
        parent = f"egg_hunt/eggs/{egg_id}"

