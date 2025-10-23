import json

with open("mysite_data.json", "r") as f:
    data = json.load(f)

# Remove all contenttypes entries
cleaned = [obj for obj in data if obj.get("model") != "contenttypes.contenttype"]

with open("mysite_data_cleaned.json", "w") as f:
    json.dump(cleaned, f, indent=2)

print(f"Cleaned fixture written to mysite_data_cleaned.json")

# incase you encounter this error:django.db.utils.IntegrityError: Problem installing fixture 
# 'C:\Windows\System32\mysite\mysite_data.json': Could not load contenttypes.ContentType(pk=8): 
# duplicate key value violates unique constraint "django_content_type_app_label_model_76bd3d3b_uniq"
#DETAIL:  Key (app_label, model)=(blog, comment) already exists.
# use this file to Clean Fix: Strip All contenttypes from the Fixture
# run :py clean_fixtures.py
# then use the cleaned file to load fixtures like this:py manage.py loaddata mysite_data_cleaned.json
