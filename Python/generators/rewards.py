import data
from save import save


def _crown(slot, count=1):
    return (
        "{"
        f"Slot: {slot}b, "
        'id: "minecraft:iron_nugget", '
        f"Count: {count}b, "
        "tag: {"
        "CustomRoleplayData: 1b, "
        "RepairCost: 0, "
        "CustomModelData: 2, "
        'display: {Name: \'{"text":"❄☠ Decked Out Crown ☠❄"}\'}'
        "}"
        "}"
    )


def rewards():
    for egg_id in data.NAMES:
        with save(f"data/do2/functions/egg_hunt/rewards/{egg_id}.mcfunction") as fd:
            # print(
            #     f"data modify storage do2_egghunt Monument.{egg_id}",
            #     "set value true",
            #     file=fd,
            # )

            # print("function do2_egghunt:update_monument", file=fd)

            reward_pos = data.LOCATIONS[egg_id]["reward_pos"]
            reward = [_crown(13, 1)]

            print("# Could be fun to have some rewards!", file=fd)

            print(
                f"# playsound minecraft:block.barrel.open master @s {reward_pos}",
                file=fd,
            )

            print(
                f"# data modify block {reward_pos} Items set value {reward}",
                file=fd,
            )

            hunter_advancement = "egg_hunt/egg_hunter"

            advancements_query = ",".join(
                f"do2:hidden/egg_hunt/eggs/{name}=true" for name in data.NAMES
            )

            print(file=fd)
            print("# Grant \"find any egg advancement.\"", file=fd)

            print("advancement grant @s only do2:hidden/egg_hunt/root", file=fd)

            
            print(file=fd)
            print("# Grant \"find all eggs advancement.\"", file=fd)
            print(
                f"execute as @s[advancements={{{advancements_query}}}]",
                f"run advancement grant @s only do2:hidden/{hunter_advancement}",
                file=fd,
            )


