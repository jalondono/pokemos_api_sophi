from core.tests.test_setup import TestSetUp


class TestRegisterViews(TestSetUp):
    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_user_can_register_correctly(self):
        res = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(res.data['email'], self.user_data['email'])
        self.assertEqual(res.status_code, 201)

    def test_user_can_login_after_verification(self):
        response = self.client.post(
            self.register_url, self.user_data, format="json")
        res = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 200)
