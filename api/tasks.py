
from celery import shared_task

from celery import shared_task
from .views import output_json
from OCR.settings import BASE_DIR

@shared_task
def process_ocr_extraction(result):
    output_json(result)
    print('Code worked properly ---------------$$$$$$$$$')
    return {"Status": True, "msg": "OCR extraction completed and result saved."}
