import os
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch, MagicMock
from .views import OCR_Extraction, StoreIntoDB

from django.core.files.uploadedfile import SimpleUploadedFile

@pytest.fixture
def sample_image():
    with open('E:/OCR/Input/1.jpg', 'rb') as file:
        image_content = file.read()
    return image_content

class OCR_ExtractionTestCase(APITestCase):
    @patch('pytesseract.image_to_data')
    @patch('pytesseract.image_to_string')
    def test_ocr_extraction_success(self, mock_image_to_string, mock_image_to_data):
        mock_image_to_data.return_value = {'text': 'Mocked OCR output'}
        mock_image_to_string.return_value = 'Mocked OCR output'
        file = SimpleUploadedFile("E:/OCR/Input/1.jpg", sample_image)
        url = reverse('ocr_extraction')
        response = self.client.post(url, {'ImagePath': file}, format='multipart')
        assert response.status_code == status.HTTP_200_OK
        assert 'FileName' in response.data
        assert 'Data' in response.data

    @patch('pytesseract.image_to_data')
    @patch('pytesseract.image_to_string')
    def test_ocr_extraction_failure(self, mock_image_to_string, mock_image_to_data):
        mock_image_to_data.side_effect = Exception("Mocked OCR error")
        mock_image_to_string.side_effect = Exception("Mocked OCR error")
        file = SimpleUploadedFile("E:/OCR/Input/1.jpg", sample_image)
        url = reverse('ocr_extraction')
        response = self.client.post(url, {'ImagePath': file}, format='multipart')
        assert response.status_code == status.HTTP_503_SERVICE_UNAVAILABLE
        assert 'msg' in response.data
        assert not response.data['Satus']

class StoreIntoDBTestCase(APITestCase):
    def test_store_into_db_success(self):
        data = {'name': 'Test Data', 'data': {'key': 'value'}}
        url = reverse('store_into_db')
        response = self.client.post(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert 'message' in response.data

    def test_store_into_db_failure(self):
        with patch.object(MyModel, 'save', side_effect=Exception("Mocked database error")):
            data = {'name': 'Test Data', 'data': {'key': 'value'}}
            url = reverse('store_into_db')
            response = self.client.post(url, data, format='json')
            assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
            assert 'error' in response.data
