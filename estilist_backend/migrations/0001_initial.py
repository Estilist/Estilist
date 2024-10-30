# Generated by Django 5.1.2 on 2024-10-30 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colorimetria',
            fields=[
                ('idcolorimetria', models.AutoField(db_column='IdColorimetria', primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, db_column='Tipo', db_comment='Ropa, Cabello, Accesorios', max_length=50, null=True)),
                ('color', models.CharField(blank=True, db_column='Color', max_length=50, null=True)),
            ],
            options={
                'db_table': 'Colorimetria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('idfeedback', models.AutoField(db_column='IdFeedback', primary_key=True, serialize=False)),
                ('ranking', models.SmallIntegerField(blank=True, db_column='Ranking', db_comment='Ranking del usuario (1-5 estrellas)', null=True)),
                ('comentarios', models.TextField(blank=True, db_column='Comentarios', null=True)),
                ('fecha', models.DateTimeField(blank=True, db_column='Fecha', null=True)),
            ],
            options={
                'db_table': 'Feedback',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ImagenesRostros',
            fields=[
                ('idimagenrostro', models.AutoField(db_column='IdImagenRostro', primary_key=True, serialize=False)),
                ('url', models.TextField(blank=True, db_column='Url', null=True)),
                ('fechasubida', models.DateTimeField(blank=True, db_column='FechaSubida', null=True)),
            ],
            options={
                'db_table': 'Imagenes_Rostros',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medidas',
            fields=[
                ('idmedidas', models.AutoField(db_column='IdMedidas', primary_key=True, serialize=False)),
                ('altura', models.DecimalField(blank=True, db_column='Altura', decimal_places=2, max_digits=5, null=True)),
                ('peso', models.DecimalField(blank=True, db_column='Peso', decimal_places=2, max_digits=5, null=True)),
                ('pecho', models.DecimalField(blank=True, db_column='Pecho', decimal_places=2, max_digits=5, null=True)),
                ('cintura', models.DecimalField(blank=True, db_column='Cintura', decimal_places=2, max_digits=5, null=True)),
                ('cadera', models.DecimalField(blank=True, db_column='Cadera', decimal_places=2, max_digits=5, null=True)),
                ('entrepierna', models.DecimalField(blank=True, db_column='Entrepierna', decimal_places=2, max_digits=5, null=True)),
                ('fechaactualizacion', models.DateTimeField(blank=True, db_column='FechaActualizacion', null=True)),
            ],
            options={
                'db_table': 'Medidas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Preferencias',
            fields=[
                ('idpreferencia', models.AutoField(db_column='IdPreferencia', primary_key=True, serialize=False)),
                ('ajusteropa', models.CharField(blank=True, db_column='AjusteRopa', max_length=50, null=True)),
                ('ropa', models.CharField(blank=True, db_column='Ropa', max_length=50, null=True)),
                ('pantalon', models.CharField(blank=True, db_column='Pantalon', max_length=50, null=True)),
                ('joyeria', models.CharField(blank=True, db_column='Joyeria', max_length=50, null=True)),
                ('calzado', models.CharField(blank=True, db_column='Calzado', max_length=50, null=True)),
            ],
            options={
                'db_table': 'Preferencias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rankings',
            fields=[
                ('idranking', models.AutoField(db_column='IdRanking', primary_key=True, serialize=False)),
                ('ranking', models.SmallIntegerField(blank=True, db_column='Ranking', db_comment='Ranking del usuario (1-5 estrellas)', null=True)),
                ('fecha', models.DateTimeField(blank=True, db_column='Fecha', null=True)),
            ],
            options={
                'db_table': 'Rankings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Recomendaciones',
            fields=[
                ('idrecomendacion', models.AutoField(db_column='IdRecomendacion', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=100, null=True)),
                ('tipo', models.CharField(blank=True, db_column='Tipo', db_comment='Ropa, Cabello, Accesorios, Outfit', max_length=50, null=True)),
                ('categoria', models.CharField(blank=True, db_column='Categoria', db_comment='Camiseta, Pantalón, Pulsera, etc.', max_length=50, null=True)),
                ('genero', models.CharField(blank=True, db_column='Genero', db_comment='Masculino, Femenino, Unisex', max_length=50, null=True)),
                ('etiquetas', models.JSONField(blank=True, db_column='Etiquetas', db_comment='Estilo, Color, Material, Temporada, Ocasión, etc.', null=True)),
                ('urlimagen', models.TextField(blank=True, db_column='UrlImagen', null=True)),
            ],
            options={
                'db_table': 'Recomendaciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sesiones',
            fields=[
                ('idsesion', models.AutoField(db_column='IdSesion', primary_key=True, serialize=False)),
                ('racha', models.SmallIntegerField(blank=True, db_column='Racha', db_comment='Contador de racha del usuario', null=True)),
                ('fechaactualizacion', models.DateTimeField(blank=True, db_column='FechaActualizacion', null=True)),
            ],
            options={
                'db_table': 'Sesiones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('idusuario', models.AutoField(db_column='IdUsuario', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=100, null=True)),
                ('apellidopaterno', models.CharField(blank=True, db_column='ApellidoPaterno', max_length=100, null=True)),
                ('apellidomaterno', models.CharField(blank=True, db_column='ApellidoMaterno', max_length=100, null=True)),
                ('correo', models.CharField(blank=True, db_column='Correo', max_length=100, null=True, unique=True)),
                ('contraseñahash', models.CharField(blank=True, db_column='ContraseñaHash', max_length=255, null=True)),
                ('edad', models.SmallIntegerField(blank=True, db_column='Edad', null=True)),
                ('genero', models.CharField(blank=True, db_column='Genero', max_length=50, null=True)),
                ('tiporostro', models.CharField(blank=True, db_column='TipoRostro', max_length=50, null=True)),
                ('tipocuerpo', models.CharField(blank=True, db_column='TipoCuerpo', max_length=50, null=True)),
                ('fecharegistro', models.DateTimeField(blank=True, db_column='FechaRegistro', null=True)),
                ('estado', models.BooleanField(blank=True, db_column='Estado', null=True)),
            ],
            options={
                'db_table': 'Usuarios',
                'managed': False,
            },
        ),
    ]