# Generated by Django 2.2.3 on 2019-08-06 10:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('state', models.CharField(default='', max_length=100)),
                ('student_name', models.CharField(max_length=100)),
                ('student_gender', models.CharField(default='', max_length=100)),
                ('student_class', models.CharField(default='', max_length=100)),
                ('question_text', models.CharField(max_length=1000)),
                ('question_format', models.CharField(max_length=100)),
                ('question_language', models.CharField(max_length=100)),
                ('contributor', models.CharField(max_length=100)),
                ('contributor_role', models.CharField(max_length=100)),
                ('context', models.CharField(max_length=100)),
                ('medium_language', models.CharField(max_length=100)),
                ('curriculum_followed', models.CharField(default='', max_length=100)),
                ('published', models.BooleanField(default=False)),
                ('published_source', models.CharField(default='', max_length=200)),
                ('published_date', models.DateField(default=datetime.date.today)),
                ('question_asked_on', models.DateField(null=True)),
                ('notes', models.CharField(default='', max_length=1000)),
                ('submission_id', models.CharField(default='', max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('field_of_interest', models.CharField(default='', max_length=100)),
                ('subject_of_session', models.CharField(default='', max_length=100)),
                ('question_topic_relation', models.CharField(default='', max_length=100)),
                ('motivation', models.CharField(default='', max_length=100)),
                ('type_of_information', models.CharField(default='', max_length=100)),
                ('source', models.CharField(default='', max_length=100)),
                ('curiosity_index', models.CharField(default='', max_length=100)),
                ('urban_or_rural', models.CharField(default='', max_length=100)),
                ('type_of_school', models.CharField(default='', max_length=100)),
                ('comments_on_coding_rationale', models.CharField(default='', max_length=500)),
                ('curated_by', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='curated_questions', to=settings.AUTH_USER_MODEL)),
                ('encoded_by', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='encoded_questions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'question',
            },
        ),
        migrations.CreateModel(
            name='UnencodedSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_id', models.IntegerField(null=True)),
                ('number_of_questions', models.IntegerField()),
                ('excel_sheet_name', models.CharField(max_length=100)),
                ('encoded', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'unencoded_submission',
            },
        ),
        migrations.CreateModel(
            name='UncuratedSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_method', models.CharField(max_length=50)),
                ('submission_id', models.IntegerField()),
                ('number_of_questions', models.IntegerField()),
                ('excel_sheet_name', models.CharField(max_length=100)),
                ('curated', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('submitted_by', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='submissions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'uncurated_submission',
            },
        ),
        migrations.CreateModel(
            name='TranslatedQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=1000)),
                ('language', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('question_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='translations', to='dashboard.Question')),
            ],
            options={
                'db_table': 'translated_question',
            },
        ),
        migrations.CreateModel(
            name='QuestionArchive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('state', models.CharField(default='', max_length=100)),
                ('student_name', models.CharField(max_length=100)),
                ('student_gender', models.CharField(default='', max_length=100)),
                ('student_class', models.CharField(default='', max_length=100)),
                ('question_text', models.CharField(max_length=1000)),
                ('question_text_english', models.CharField(default='', max_length=1000)),
                ('question_format', models.CharField(max_length=100)),
                ('question_language', models.CharField(max_length=100)),
                ('contributor', models.CharField(max_length=100)),
                ('contributor_role', models.CharField(max_length=100)),
                ('context', models.CharField(max_length=100)),
                ('medium_language', models.CharField(max_length=100)),
                ('curriculum_followed', models.CharField(default='', max_length=100)),
                ('published', models.BooleanField(default=False)),
                ('published_source', models.CharField(default='', max_length=200)),
                ('published_date', models.DateField(default=datetime.date.today)),
                ('question_asked_on', models.DateField(null=True)),
                ('notes', models.CharField(default='', max_length=1000)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('submitted_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='archived_questions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'question_archive',
            },
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_count', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('submitted_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='submitted_datasets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('answered_by', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='submitted_answers', to=settings.AUTH_USER_MODEL)),
                ('approved_by', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='approved_answers', to=settings.AUTH_USER_MODEL)),
                ('question_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='answers', to='dashboard.Question')),
            ],
            options={
                'db_table': 'answer',
            },
        ),
    ]
