from django.test import TestCase, Client
from django.urls import reverse
from users.models import CustomUser, Order


class RegisterTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('users:register')

    def test_register_GET(self):
        # 测试GET请求
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register/register.html')

    def test_register_POST_valid(self):
        # 测试有效的POST请求
        response = self.client.post(self.register_url, {
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'password1': 'verysecurepassword',
            'password2': 'verysecurepassword',
        })
        self.assertEqual(response.status_code, 302)  # Assuming it redirects after successful registration

    def test_register_POST_invalid(self):
        # 测试无效的POST请求
        response = self.client.post(self.register_url, {
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'password1': 'verysecurepassword',
            'password2': 'notthesame',
        })
        self.assertEqual(response.status_code, 200)  # Stays on the same page if there is a form error

    def tearDown(self):
        # Your tear down actions (if any)
        pass
class LoginViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('users:login')
        self.user = CustomUser.objects.create_user(email='testuser@example.com', password='12345')

    def test_login_view_GET(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/login.html')

    def test_login_view_POST_valid(self):
        response = self.client.post(self.login_url, {'username': 'testuser@example.com', 'password': '12345'})
        self.assertEqual(response.status_code, 302)

    def test_login_view_POST_invalid(self):
        response = self.client.post(self.login_url, {'username': 'testuser@example.com', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', None, 'Please enter a correct username and password. Note that both fields may be case-sensitive.')

    def tearDown(self):
        self.user.delete()
class DownloadTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', password='12345')
        self.download_url = reverse('users:download')  # Make sure to provide the correct URL name
        # 假设已经创建了Order实例和相关文件
        self.order = Order.objects.create(...)  # Fill in the creation details
        self.client.login(username='testuser', password='12345')

    def test_download_authenticated_user(self):
        # 测试认证用户的文件下载
        response = self.client.get(self.download_url, {'order_number': self.order.order_number})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response['Content-Disposition'].startswith('inline; filename='))

    def test_download_unauthenticated_user(self):
        # 测试未认证用户的文件下载行为
        self.client.logout()
        response = self.client.get(self.download_url, {'order_number': self.order.order_number})
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('users:login'))

    def tearDown(self):
        # 清理创建的测试数据
        self.order.delete()
        self.user.delete()
