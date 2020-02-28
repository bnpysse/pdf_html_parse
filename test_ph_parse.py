from unittest import TestCase
from ph_parse import Foo, ParseHtml, Contact, Files


# class TestParseHtml(TestCase):
#     def test_parse_contact(self):
#         self.skipTest('this is ')
#
#     def test_parse_name(self):
#         self.fail()
#
#     def test_parse_experience(self):
#         self.fail()
#

def test_money():
    assert Foo.money, 100


def test_parse_contact():
    assert True


def test_parse_name():
    assert True


def test_parse_experience():
    assert True


def test_parse_education():
    assert True


def test_page_sep():
    assert ParseHtml.PageSep, '.t.m0.x0.h1'


def test_html_file_list():
    files = Files()
    file_name = files.dir + '/' + files.HtmlFileList[0]

    assert file_name, files.dir + '/' + 'Aakanksha_Joshi_AEMAABDt9AsB6TqGNVcSJV0l3EbZU7DqX7eQPQw.html'


def test_contact():
    files = Files()
    file_name = files.dir + '/' + files.HtmlFileList[0]
    print(file_name)
    contact = Contact(file_name=file_name)

    assert contact, 'www.linkedin.com/in/aakanksha-'


def test_contact():
    contact = Contact(file_name=ParseHtml.HtmlFileList[0])
