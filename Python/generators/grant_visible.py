from save import save
import data


def grant_visible():
    with save("data/do2/functions/advancements/grant_visible/adventuring.mcfunction") as fd:
        advancements = ["root", "egg_hunter"]
        advancements.extend(f"eggs/{egg_id}" for egg_id in data.NAMES)

        for advancement_id in advancements:
            print(
                "execute as @s[advancements={"
                f"do2:visible/egg_hunt/{advancement_id}=false,"
                f"do2:hidden/egg_hunt/{advancement_id}=true}}] "
                f"run advancement grant @s only do2:visible/egg_hunt/{advancement_id}",
                file=fd,
            )

