from save import save
import data


OFFSETS = {
    "0": (0, 0, 0),
    "+x": (0.2, 0, 0),
    "-x": (-0.2, 0, 0),
    "+z": (0, 0, 0.2),
    "-z": (0, 0, -0.2),
    "cleo": (0, -0.33, -0.3),
}


def spawn_egg_hitboxes():
    with save("data/do2/functions/egg_hunt/spawn_egg_hitboxes.mcfunction") as fd:
        print("kill @e[type=minecraft:armor_stand,tag=do2.egg_hunt.is_hitbox]", file=fd)

        for locations in [data.LOCATIONS]:
            for egg_id, location in locations.items():
                if location["egg"] == "":
                    continue

                x, y, z = map(int, location["egg"].split())
                dx, dy, dz = OFFSETS[location["egg_direction"]]

                print(
                    f"summon minecraft:armor_stand {x + 0.5 + dx} {y - 1.33 + dy} {z + 0.5 + dz}",
                    "{",
                    f'Tags:["do2.egg_hunt.is_hitbox", "do2.egg_hunt.is_{egg_id}_hitbox"],'
                    "Invisible: true,",
                    "Invulnerable: true,",
                    "NoAI: true,",
                    "NoGravity: true",
                    "}",
                    file=fd,
                )

