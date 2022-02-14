

from django.test import SimpleTestCase

from django.urls import reverse ,resolve
from mainapp import views


print("starting test url...")
class TestUrls(SimpleTestCase):
    #url name: indexpage
    def test_indexpage_url_is(self):
        url=reverse('indexpage')
        self.assertEquals(resolve(url).func,views.Indexpage)

    #url name: llogin
    def test_llogin_url_is(self):
        url=reverse('llogin')
        self.assertEquals(resolve(url).func,views.Loginer)
    #url name: logout
    def test_logout_url_is(self):
        url=reverse('logout')
        self.assertEquals(resolve(url).func,views.Logouter)
    #url name: usercreate
    def test_usercreate_url_is(self):
        url=reverse('usercreate')
        self.assertEquals(resolve(url).func,views.UserCreator)
    #url name: congratulations
    def test_usercreate_url_is(self):
        url=reverse('congratulations')
        self.assertEquals(resolve(url).func,views.Congratulatory)
    #url name: activator
    def test_staff_url_is(self):
        url=reverse('staff')
        self.assertEquals(resolve(url).func,views.Staff)



print("finished test urls")