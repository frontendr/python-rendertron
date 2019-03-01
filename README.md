# Python Rendertron

> Rendertron middleware for Python applications.

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

Install a Rendertron service by following the steps in [the documentation](https://github.com/GoogleChrome/rendertron#installing--deploying).

The goal is to publish this package to PyPI once it is stable. Until then
install it using `pip`'s `-e` flag:

```bash
pip install -e git://git@github.com:frontendr/python-rendertron.git@develop#egg=rendertron
```

This will install the `develop` branch.

The next steps depend on your framework of choice.

### Django

1. Add `'rendertron'` to the `INSTALLED_APPS` list in settings.
2. Add `'rendertron.middleware.DjangoRendertronMiddleware'` to the `MIDDLEWARE`
list in the settings.
3. Configure settings

#### Django settings

- `RENDERTRON_URL` - Default: `'http://localhost:3000/'`. The url the Rendertron
service is listening on.
- `RENDERTRON_STORAGE`
- `RENDERTRON_RENDER_QUERY_PARAM` - Default: `'rendertron_render'`. The query
parameter added to the request url passed to Rendertron. This is used to
differentiate normal requests with requests from Rendertron.
