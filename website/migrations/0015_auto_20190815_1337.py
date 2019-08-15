# Generated by Django 2.2.4 on 2019-08-15 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20190810_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='nascimento_aluno',
            field=models.DateField(verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='turma_aluno',
            field=models.CharField(max_length=255, verbose_name='Turma do Aluno'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='from_email',
            field=models.EmailField(max_length=255, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='message',
            field=models.TextField(verbose_name='Mensagem'),
        ),
        migrations.AlterField(
            model_name='escola',
            name='codigo_acesso',
            field=models.CharField(error_messages={'unique': 'Código de acesso já existente.'}, max_length=12, unique=True, verbose_name='Código de acesso'),
        ),
        migrations.AlterField(
            model_name='escola',
            name='confirmar_senha',
            field=models.CharField(max_length=12, verbose_name='Confirme a senha de acesso'),
        ),
        migrations.AlterField(
            model_name='escola',
            name='diretor_responsavel',
            field=models.CharField(max_length=255, verbose_name='Diretor Responsável'),
        ),
        migrations.AlterField(
            model_name='escola',
            name='senha_acesso',
            field=models.CharField(max_length=12, verbose_name='Senha de acesso'),
        ),
    ]
