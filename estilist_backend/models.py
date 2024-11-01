from django.db import models

# Create your models here.

class Usuarios(models.Model):
    idusuario = models.AutoField(db_column='IdUsuario', primary_key=True)  # Field name made lowercase.
    idlogin = models.ForeignKey('auth.User', models.DO_NOTHING, db_column='id', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apellidopaterno = models.CharField(db_column='ApellidoPaterno', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apellidomaterno = models.CharField(db_column='ApellidoMaterno', max_length=100, blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    edad = models.SmallIntegerField(db_column='Edad', blank=True, null=True)  # Field name made lowercase.
    genero = models.CharField(db_column='Genero', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tiporostro = models.CharField(db_column='TipoRostro', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tipocuerpo = models.CharField(db_column='TipoCuerpo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fecharegistro = models.DateTimeField(db_column='FechaRegistro', blank=True, null=True)  # Field name made lowercase.
    pais = models.CharField(db_column='Pais', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Usuarios'

class Colorimetria(models.Model):
    idcolorimetria = models.AutoField(db_column='IdColorimetria', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='IdUsuario', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=50, blank=True, null=True, db_comment='Ropa, Cabello, Accesorios')  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Colorimetria'


class Feedback(models.Model):
    idfeedback = models.AutoField(db_column='IdFeedback', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='IdUsuario', blank=True, null=True)  # Field name made lowercase.
    ranking = models.SmallIntegerField(db_column='Ranking', blank=True, null=True, db_comment='Ranking del usuario (1-5 estrellas)')  # Field name made lowercase.
    comentarios = models.TextField(db_column='Comentarios', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Feedback'


class ImagenesRostros(models.Model):
    idimagenrostro = models.AutoField(db_column='IdImagenRostro', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='IdUsuario', blank=True, null=True)  # Field name made lowercase.
    url = models.TextField(db_column='Url', blank=True, null=True)  # Field name made lowercase.
    fechasubida = models.DateTimeField(db_column='FechaSubida', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Imagenes_Rostros'


class Medidas(models.Model):
    idmedidas = models.AutoField(db_column='IdMedidas', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='IdUsuario', blank=True, null=True)  # Field name made lowercase.
    altura = models.DecimalField(db_column='Altura', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    peso = models.DecimalField(db_column='Peso', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pecho = models.DecimalField(db_column='Pecho', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cintura = models.DecimalField(db_column='Cintura', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cadera = models.DecimalField(db_column='Cadera', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    entrepierna = models.DecimalField(db_column='Entrepierna', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fechaactualizacion = models.DateTimeField(db_column='FechaActualizacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Medidas'


class Preferencias(models.Model):
    idpreferencia = models.AutoField(db_column='IdPreferencia', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='IdUsuario', blank=True, null=True)  # Field name made lowercase.
    ajusteropa = models.CharField(db_column='AjusteRopa', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ropa = models.CharField(db_column='Ropa', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pantalon = models.CharField(db_column='Pantalon', max_length=50, blank=True, null=True)  # Field name made lowercase.
    joyeria = models.CharField(db_column='Joyeria', max_length=50, blank=True, null=True)  # Field name made lowercase.
    calzado = models.CharField(db_column='Calzado', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Preferencias'

class Recomendaciones(models.Model):
    idrecomendacion = models.AutoField(db_column='IdRecomendacion', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=50, blank=True, null=True, db_comment='Ropa, Cabello, Accesorios, Outfit')  # Field name made lowercase.
    categoria = models.CharField(db_column='Categoria', max_length=50, blank=True, null=True, db_comment='Camiseta, Pantalón, Pulsera, etc.')  # Field name made lowercase.
    genero = models.CharField(db_column='Genero', max_length=50, blank=True, null=True, db_comment='Masculino, Femenino, Unisex')  # Field name made lowercase.
    etiquetas = models.JSONField(db_column='Etiquetas', blank=True, null=True, db_comment='Estilo, Color, Material, Temporada, Ocasión, etc.')  # Field name made lowercase.
    urlimagen = models.TextField(db_column='UrlImagen', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Recomendaciones'

class Rankings(models.Model):
    idranking = models.AutoField(db_column='IdRanking', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='IdUsuario', blank=True, null=True)  # Field name made lowercase.
    idrecomendacion = models.ForeignKey('Recomendaciones', models.DO_NOTHING, db_column='IdRecomendacion', blank=True, null=True)  # Field name made lowercase.
    ranking = models.SmallIntegerField(db_column='Ranking', blank=True, null=True, db_comment='Ranking del usuario (1-5 estrellas)')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Rankings'

class Sesiones(models.Model):
    idsesion = models.AutoField(db_column='IdSesion', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='IdUsuario', blank=True, null=True)  # Field name made lowercase.
    racha = models.SmallIntegerField(db_column='Racha', blank=True, null=True, db_comment='Contador de racha del usuario')  # Field name made lowercase.
    fechaactualizacion = models.DateTimeField(db_column='FechaActualizacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sesiones'


