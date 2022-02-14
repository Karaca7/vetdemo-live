




from django.test import TestCase,Client

from django.urls import reverse



print("starting test views...")

from django.contrib.auth.models import User
class TestViews(TestCase):
    def setUp(self):
            self.client=Client()
            self.indexpage_url=reverse('indexpage')
            self.llogin=reverse('llogin')
            self.usercreate=reverse('usercreate')
            self.congratulations=reverse('congratulations')
            self.staff=reverse("staff")
            self.TEMPUSER = {
            'username': 'testuser',
            'password': 'secret'}
            User.objects.create_user(**self.TEMPUSER)


    def test_indexpage_GET(self):     
        response=self.client.get(self.indexpage_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'mainapp/index.html')

    def test_llogin_GET(self):     
        response=self.client.get(self.llogin)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'mainapp/user/login.html')

    def test_usercreate_GET(self):     
        response=self.client.get(self.usercreate)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'mainapp/user/usercreate.html')

    def test_congratulations_GET(self):     
        response=self.client.get(self.congratulations)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'mainapp/user/congratulations.html')



    def test_llogin_POST(self):
        print(self.llogin)
        response=self.client.post(self.llogin,self.TEMPUSER,follow=True)  
        self.assertTemplateUsed(response,'mainapp/index.html')
        self.assertTrue(response.context['user'].is_active) 



