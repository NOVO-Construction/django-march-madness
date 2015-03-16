# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bracket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(max_length=4)),
                ('seed', models.IntegerField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('tie_break', models.IntegerField(max_length=3)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EntryPick',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entry', models.ForeignKey(to='madness.Entry')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_1_score', models.IntegerField(max_length=4, blank=True)),
                ('team_2_score', models.IntegerField(max_length=4, blank=True)),
                ('team_1', models.ForeignKey(related_name='+', to='madness.Bracket')),
                ('team_2', models.ForeignKey(related_name='+', to='madness.Bracket')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('grid', models.IntegerField(max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ScoreLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('espn', models.IntegerField(max_length=11)),
                ('cbs', models.IntegerField(max_length=11)),
                ('ncaa', models.IntegerField(max_length=11)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Standing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField()),
                ('prev_position', models.IntegerField(blank=True)),
                ('points', models.IntegerField(default=0)),
                ('entry', models.ForeignKey(to='madness.Entry')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('mascot', models.CharField(max_length=100)),
                ('abbreviation', models.CharField(max_length=4)),
                ('score_link', models.ForeignKey(to='madness.ScoreLink')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='entrypick',
            name='game',
            field=models.ForeignKey(to='madness.Game'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entrypick',
            name='pick',
            field=models.ForeignKey(to='madness.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bracket',
            name='region',
            field=models.ForeignKey(to='madness.Region'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bracket',
            name='team',
            field=models.ForeignKey(to='madness.Team'),
            preserve_default=True,
        ),
    ]
