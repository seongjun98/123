# Generated by Django 4.2 on 2023-05-12 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Signup", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=50, unique=True)),
                ("password", models.CharField(max_length=50)),
                ("hospital", models.DateTimeField(max_length=50)),
                ("tel", models.CharField(max_length=50)),
                ("type", models.CharField(max_length=50)),
                ("country", models.CharField(max_length=50)),
            ],
            options={"db_table": "users",},
        ),
        migrations.DeleteModel(name="signup",),
    ]
