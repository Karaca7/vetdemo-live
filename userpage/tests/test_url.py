

from django.test import SimpleTestCase

from django.urls import reverse ,resolve
from userpage import views

class TestUrls(SimpleTestCase):
    

    def test_main_url_is(self):
        url=reverse("main")
        self.assertEquals(resolve(url).func,views.Userp)

    def test_addpet_url_is(self):
          url=reverse("addpet")
          self.assertEquals(resolve(url).func,views.Addpet)

    def test_addpetowner_url_is(self):
          url=reverse("addpetowner")
          self.assertEquals(resolve(url).func,views.AddPetOwner)

    def test_updatepet_url_is(self):
          url=reverse("updatepet",kwargs={"id":1}) #is random id
          self.assertEquals(resolve(url).func,views.UpdatePet)
    

    def test_deletepet_url_is(self):
          url=reverse("deletepet",kwargs={"id":1}) #is random id
          self.assertEquals(resolve(url).func,views.DeletePet)