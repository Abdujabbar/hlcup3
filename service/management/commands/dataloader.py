from django.core.management.base import BaseCommand
import zipfile
import json, time
from service.service_factory import ServiceFactory


class Command(BaseCommand):
    help = 'just run it!'

    def handle(self, *args, **options):
        start_time = time.time()
        data_zip = open('/tmp/data/data.zip', 'rb')
        zipped_files = zipfile.ZipFile(data_zip)
        for file in zipped_files.namelist():
            if file.find('.txt') != -1:
                continue
            body = json.loads(zipped_files.read(file))
            for account in body['accounts']:
                try:
                    ServiceFactory.create_account_with_relationships(account)
                except Exception as e:
                    print(e)
        elapsed_time = time.time() - start_time
        print(elapsed_time)
