from distutils.core import setup

setup(
    name = "django-ogp",
    version = '0.1',
    url = 'https://bitbucket.org/liberation/django-ogp/changesets',
    author = 'Liberation',
    author_email= '',
    long_description=open('README.md').read(),
    description = 'Integrate OpenGraphProtocol meta tags in your Django project',
    packages = ['django-ogp']
)

