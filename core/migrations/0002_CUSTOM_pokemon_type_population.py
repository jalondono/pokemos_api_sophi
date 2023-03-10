from django.db import migrations, models


def migrate_pokemon_types(apps, schema_editor):
    pokemon_types = [
        "Normal",
        "Fire",
        "Water",
        "Grass",
        "Electric",
        "Ice",
        "Fighting",
        "Poison",
        "Ground",
        "Flying",
        "Psychic",
        "Bug",
        "Rock",
        "Ghost",
        "Dark",
        "Dragon",
        "Steel",
        "Fairy",
    ]

    enum_pokemon_type_model: models.Model = apps.get_model("core", "EnumPokemonType")

    for pokemon_type in pokemon_types:
        enum_pokemon_type_model.objects.create(name=pokemon_type)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(code=migrate_pokemon_types, reverse_code=migrations.RunPython.noop),
    ]
