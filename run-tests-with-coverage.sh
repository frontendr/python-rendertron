#!/usr/bin/env bash
coverage run `which django-admin` test --pythonpath . --settings tests.django.settings
