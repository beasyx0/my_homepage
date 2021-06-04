from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0006_post_search_vector'),
    ]
    operations = [
        migrations.RunSQL('CREATE EXTENSION IF NOT EXISTS pg_trgm'),
    ]