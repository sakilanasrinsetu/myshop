from django import template
import datetime
from middlewares.middlewares import RequestMiddleware
from django.contrib.auth.models import User
import json
import re
from dashboard.models import *


register = template.Library()


@register.filter
def remove_id(value):
    if "_id" in value:
        return value.replace("_id", "")
    else:
        return value.replace(" id", "")


@register.simple_tag(takes_context=True)
def user_has_perm(context, permission):
    request = context['request']
    if request.user.has_perm(permission) == True:
        return True
    return False


@register.filter
def to_title(value):
    result = value.replace("_", " ").title()
    return result


@register.filter
def get_expire_in(value):
    # extract expire date time
    token_timestamp = int(value.get("expires", 0))
    token_expire_date = datetime.datetime.strptime(
        datetime.datetime.utcfromtimestamp(token_timestamp).strftime(
            '%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S'
    )
    current_datetime = datetime.datetime.now()
    remaining_datetime = (token_expire_date - current_datetime)
    result = None
    if remaining_datetime.days >= 0:
        result = f"{remaining_datetime.days} Days, {remaining_datetime.seconds//3600} Hours, {(remaining_datetime.seconds//60)%60} Minutes"
    else:
        result = "Expired"
    return result


@register.filter
def get_file_type(value):
    if type(value) == str:
        values = value.split(".")
        file_extension = values[-1]
        image_file_extensions = ["jpg", "jpeg", "png", "gif"]
        doc_file_extensions = ["doc", "docx"]
        pdf_file_extensions = ["pdf"]
        if file_extension.lower() in image_file_extensions:
            return "image"
        elif file_extension.lower() in doc_file_extensions:
            return "document"
        elif file_extension.lower() in pdf_file_extensions:
            return "pdf"
        else:
            return "unknown"
    

@register.filter
def truncate_word(value, numWords):
    if value:
        return value[:numWords] + " ..."
    else:
        return "--"


@register.filter
def remove_html_tags(text):
    """
    remove_html_tags() => Removes HTML Markup Tags
    """
    tag = False
    quote = False
    out = ""

    for c in text:
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote:
            tag = False
        elif (c == '"' or c == "'") and tag:
            quote = not quote
        elif not tag:
            out = out + c

    return out

