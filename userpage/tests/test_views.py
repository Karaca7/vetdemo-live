


from django.test import TestCase,Client

from django.urls import reverse

from django.contrib.auth.models import User

class TestViews(TestCase):
    

    def setUp(self):
            self.client=Client()
            self.main=reverse("main")
            self.addpet=reverse("addpet")
            self.addpetowner=reverse("addpetowner")
            self.TEMPUSER = {
            'username': 'testuser',
            'password': 'secret'}
            user=User.objects.create_user(**self.TEMPUSER)
          

    def test_main_GET(self):

        self.client.login(**self.TEMPUSER)
        response=self.client.get(self.main,self.TEMPUSER,follow=True)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'userpage/userpage.html')


    def test_addpet_GET(self):

        self.client.login(**self.TEMPUSER)
        response=self.client.get(self.addpet,self.TEMPUSER,follow=True)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'userpage/addpet.html')


    def test_addpetowner_GET(self):
        self.client.login(**self.TEMPUSER)
        response=self.client.get(self.addpetowner,self.TEMPUSER,follow=True)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'userpage/addpetowner.html')


    def test_updatepet_GET(self):
        self.client.login(**self.TEMPUSER)
        response=self.client.get("/user/updatepet/7",self.TEMPUSER,follow=True)
        self.assertEquals(response.status_code,200,)
        self.assertTemplateUsed(response,'userpage/userpage.html')


    def test_updatepet_POST(self):
        self.client.login(**self.TEMPUSER)
        
        response=self.client.post("/user/updatepet/7",self.TEMPUSER,follow=True)
        
        self.assertEquals(response.status_code,200,)
        self.assertTemplateUsed(response,'userpage/userpage.html')

    def test_deletepet_POST(self):
        self.client.login(**self.TEMPUSER)
       
        response=self.client.post("/user/deletepet/7",self.TEMPUSER,follow=True)
        
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'userpage/userpage.html')

  