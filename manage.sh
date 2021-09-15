#!/bin/bash

cur_dir=$(pwd)

if [[ "${cur_dir}" == *"django-tutorial/mysite"* ]]; then
    python manage.py $@
else
    python mysite/manage.py $@
fi