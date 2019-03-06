# Python Rendertron

> Rendertron middleware for Python applications.

[![Build Status](https://travis-ci.org/frontendr/babel-plugin-transform-compress-graphql.svg?branch=master)](https://travis-ci.com/frontendr/python-rendertron.svg)
[![Coverage Status](https://coveralls.io/repos/github/frontendr/python-rendertron/badge.svg?branch=develop)](https://coveralls.io/github/frontendr/python-rendertron?branch=develop)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

[Rendertron](https://github.com/GoogleChrome/rendertron) is a headless Chrome 
rendering solution designed to render & serialise web pages on the fly. The
goal of this package is to provide middleware to render a request using a
Rendertron service and make the result available.

This makes it possible to for example render Progressive Web Apps (PWA), wait
for it to fully render (completes initial data loading etc.) and use that
fully built markup as a response.

Besides the fact that your user will see a fully rendered application faster it
also allows search engines to properly index the markup. 

## Installing

Install a Rendertron service by following the steps in
[the documentation](https://github.com/GoogleChrome/rendertron#installing--deploying).

Install this package using `pip`:
```bash
pip install rendertron
```

You can also install the latest development version using `pip`'s `-e` flag:

```bash
pip install -e git://git@github.com:frontendr/python-rendertron.git@develop#egg=rendertron
```

This will install the `develop` branch.

### Django

1. Add `'rendertron'` to the `INSTALLED_APPS` list in settings.
2. Add `'rendertron.middleware.DjangoRendertronMiddleware'` to the `MIDDLEWARE`
list in the settings.

## Configuration

Most configuration is done by specifying specific variables. For Django users
that's done in your site's settings.

The following settings are available:

| Setting | Default | Description |
|---------|---------|-------------|
| `RENDERTRON_BASE_URL` | `'http://localhost:3000/'` | The url the Rendertron service is listening on. |
| `RENDERTRON_RENDER_QUERY_PARAM` | `'rendertron_render'` | The query parameter added to the request url passed to Rendertron. This is used to differentiate normal requests with requests from Rendertron. |
| `RENDERTRON_STORAGE` | See Storage | An object literal specifying and configuring the storage class to be used. See the Storage section for more information. |
| `RENDERTRON_INCLUDE_PATTERNS` | `[]` | A list of regular expression patterns to include. Once a pattern in this list matches the request no further checking will be done. |
| `RENDERTRON_EXCLUDE_PATTERNS` | List of common extensions. | By default this is a list of common static file type extensions used on the web. If Django is detected it's `STATIC_URL` and `MEDIA_URL` paths are added to the list. Note that if you override this setting all defaults are gone. If you want to keep these defaults *and* add your own patterns use `RENDERTRON_EXCLUDE_PATTERNS_EXTRA`.
| `RENDERTRON_EXCLUDE_PATTERNS_EXTRA` | `[]` | Like `RENDERTRON_EXCLUDE_PATTERNS` but will be appended to that list. |

## Storage

Storage classes are handling the logic of storing the results coming from the
Rendertron service for a period of time. They handle if, how, where and how
long a result is stored. There are some core storage classes available the
system is built for it to be very easy to built your own.

The choice of one of the built in storage classes depends on your framework.

### Any framework: `DummyStorage`

A storage class that doesn't do anything. It doesn't store and will never return
a stored result.

To use it simply set `RENDERTRON_STORAGE['CLASS']` to
`'rendertron.storage.DummyStorage'`. It has no options.

### Django: `DjangoCacheStorage`

A storage class that utilizes Django's cache framework to store the results.

To use it simply set `RENDERTRON_STORAGE['CLASS']` to
`'rendertron.storage.DjangoCacheStorage'`. It has the following options:

| Setting | Default | Description |
|---------|---------|-------------|
| `TIMEOUT` | Django's `DEFAULT_TIMEOUT` cache setting which is `300` (5 minutes) | The number of seconds the result should be stored in the cache. It's the `timeout` argument for Django's [`cache.set`](https://docs.djangoproject.com/en/dev/topics/cache/#django.core.caches.cache.set) method. |
| `VERSION` | `None` | The `version` argument which is passed to Django's [`cache.set`](https://docs.djangoproject.com/en/dev/topics/cache/#django.core.caches.cache.set) method. |

Example config:

```python
RENDERTRON_STORAGE = {
    'CLASS': 'rendertron.storage.DjangoCacheStorage',
    'OPTIONS': {
        'TIMEOUT': 300,
    }
}
```

## Running tests

First install Django to be able to test Django related things.

```bash
pip install django
```

Then run the tests via `django-admin` using the provided minimal settings file.

```bash
django-admin test --pythonpath . --settings tests.django.settings
```

## License

MIT
