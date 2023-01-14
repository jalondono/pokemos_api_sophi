from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from core.tests.utils import ErrorReporterMixin


class RESTTestCase(TestCase, APIClient, ErrorReporterMixin):
    """
    Base class what provide basic http method with their respective tests
    """
    def detail_url(self, obj_id, uri):
        return f"{uri}{obj_id}/"

    def do_post_test_request(self, payload, uri=None):
        # Do post
        response = self.client.post(uri, payload, content_type='application/json')
        # Check response
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
            self.error_message(response.status_code, status.HTTP_201_CREATED, "POST", uri, payload, response.data),
        )
        return response.data

    def do_patch_test_request(self, payload, obj_id, uri=None):
        # Do patch
        uri = self.detail_url(obj_id=obj_id, uri=uri)
        response = self.client.patch(uri, payload, content_type='application/json')
        # Check response
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            self.error_message(response.status_code, status.HTTP_200_OK, "PATCH", uri, payload, response.data),
        )
        return response.data

    def do_delete_test_request(self, obj_id, uri):
        uri = self.detail_url(uri=uri, obj_id=obj_id)
        response = self.client.delete(uri)
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
            self.error_message(response.status_code, status.HTTP_204_NO_CONTENT, "DELETE", uri, "", response.data),
        )
        return response.data

    def do_get_test_request(self, obj_id, uri):
        uri = self.detail_url(uri=uri, obj_id=obj_id)
        response = self.client.get(uri)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            self.error_message(response.status_code, status.HTTP_200_OK, "GET", uri, "", response.data),
        )
        return response.data
