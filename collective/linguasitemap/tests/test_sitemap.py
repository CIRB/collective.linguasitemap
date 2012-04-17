import unittest2 as unittest

from zope import component
from collective.linguasitemap.tests import base, utils
from plone.testing.z2 import Browser

class UnitTestSiteMap(unittest.TestCase):
    
    def test_language(self):
        from collective.linguasitemap.browser import sitemap
        sm = sitemap.SiteMapView(utils.FakeContext(), None)
        self.assertEqual(sm.language, 'all')

class IntegrationTestSiteMap(base.IntegrationTestCase):
    """The name of the class should be meaningful. This may be a class that
    tests the installation of a particular product.
    """

    def test_language(self):
        from collective.linguasitemap.browser import sitemap
        sm = sitemap.SiteMapView(self.portal, self.portal.REQUEST)
        self.assertEqual(sm.language,'all')

        #FIXME: theses tests fails... don't know why
        sm = component.getMultiAdapter((self.portal, self.portal.REQUEST),
                                       name="sitemap.xml.gz")
        self.assertEqual(sm.language,'all')

        sm = self.portal.restrictedTraverse('@@sitemap.xml.gz')
        self.assertEqual(sm.language,'all')

class FunctionaTestSiteMap(base.FunctionalTestCase):
    """The name of the class should be meaningful. This may be a class that
    tests the installation of a particular product.
    """

    def test_language(self):
        browser = Browser(self.layer['app'])
        sm = browser.open(self.portal.absolute_url()+'/sitemap.xml.gz')
        self.assertFalse(browser.isHtml)
        self.assert_(len(browser.contents)>0)
        #TODO: open the gzip and then parse the xml and then verify content

def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
