### Integrate [OpenGraphProtocol](http://ogp.me) meta tags in your Django project

Forked from bitbucket repo on https://bitbucket.org/liberation/django-ogp
All credits to liberation @ bitbucket

#### The setup ####

First install the django\_ogp app using pip and add it to your INSTALLED\_APPS.
Then load __{% ogp_tags %}__ in your pages, you'll have access to 2 tags:

* __{% ogp_namespace %}__ which allows you to populate your __html__ tag with the right namespace attribute
* __{% render_ogp item %}__ which allows you to render __meta__ tags related to your item

For a concrete example:

    {% load ogp_tags %}
    <html {% ogp_namespace %}>
    <head>
      <title>My page</title>
      {% render_ogp item %}
    </head>
    <body>foo</body>
    </html>

Will produce:

    <html xmlns:og="http://ogp.me/ns#">
    <head>
      <title>My page</title>
      <meta property="og:title" content="The Rock" />
      <meta property="og:type" content="movie" />
      <meta property="og:url" content="http://www.imdb.com/title/tt0117500/" />
      <meta property="og:image" content="http://ia.media-imdb.com/images/rock.jpg" />
    </head>
    <body>foo</body>
    </html>

Now you probably wonder where all this content comes from. 
Given that the __item__ object is an instance of a class (let's say a model),
you have to put an __ogp\_enabled__ attribute on it and define methods starting with ogp\_*:

    class MyModel(models.Model):
        # Fields
        ogp_enabled = True
        
        def ogp_title(self):
              return 'The Rock'

        def ogp_type(self):
            return 'movie'
        
        def ogp_url(self):
            return 'http://www.imdb.com/title/tt0117500/'
        
        def ogp_image(self):
            return 'http://ia.media-imdb.com/images/rock.jpg'

Those 4 OGP properties (title, type, url and image) are required but 
you can add additionnal infos as suggested on 
[the dedicated website](http://ogp.me):

    class MyCompleteModel(MyModel):
        def ogp_latitude(self):
            return 37.416343

        def ogp_longitude(self):
            return -122.153013

        def ogp_video_width(self):
          return ("video:width", 1024)
        
        def ogp_video_height(self):
            return ("video:height", 800)
        
        def ogp_site_name(self):
            return "My Website"
        
        def ogp_postal_code(self):
            return ("postal-code", 13200)

    
Will produce:

    <html xmlns:og="http://ogp.me/ns#">
    <head>
      <title>My page</title>
      <meta property="og:title" content="The Rock" />
      <meta property="og:type" content="movie" />
      <meta property="og:url" content="http://www.imdb.com/title/tt0117500/" />
      <meta property="og:image" content="http://ia.media-imdb.com/images/rock.jpg" />
      
      <meta property="og:latitude" content="37.416343" />
      <meta property="og:longitude" content="-122.153013" />
      <meta property="og:video:height" content="640" />
      <meta property="og:video:width" content="385" />
      <meta property="og:site_name" content="My Website" />
      <meta property="og:postal-code" content="13200" />
    </head>
    <body>foo</body>
    </html>

Note that due to inconsistencies in OGP's properties' names, we can't guess
the property from the method name so you can return a tuple with a string
as the first element which will be used for the property. Otherwise, the name
of the method (minus ogp\_ will be used).

Pro tip, you can probably reuse existing methods in your models:

    class MyExistingModel(models.Model):
        def __unicode__(self):
            return u'%(first_name)s %(last_name)s' % self.__dict__
        ogp_title = __unicode__
        
        @models.permalink
        def get_absolute_url(self):
            return ('app:resource', [self.id,])
        
        def ogp_url(self):
            return settings.BASE_URL + self.get_absolute_url()
        
        def ogp_image(self):
            if not self.image:
                return None  # will not render the meta tag in the template

And so on.


#### The discussion ####

Suggestions? Let's discuss in the Issues tab.
