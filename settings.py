from config.nosqlcfg import mongodb
from config.config import api_cfg

MONGO_URI = mongodb['url']

URL_PREFIX = api_cfg['url_prefix']
API_VERSION = api_cfg['api_version']
QUERY_WHERE = 'where'
JSON = True
XML = False
# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'firstname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
    },
    'lastname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
        'required': True,
        # talk about hard constraints! For the purpose of the demo
        # 'lastname' is an API entry-point, so we need it to be unique.
        'unique': True,
    },
    'age': {
        'type': 'integer',
    },
    # 'role' is a list, and can only contain values from 'allowed'.
    'role': {
        'type': 'list',
        'allowed': ["author", "contributor", "copy"],
    },
    # An embedded 'strongly-typed' dictionary.
    'location': {
        'type': 'dict',
        'schema': {
            'address': {'type': 'string'},
            'city': {'type': 'string'}
        },
    },
    'born': {
        'type': 'datetime',
    },
    'lbs': {
        'type': 'point'
    },
}

moive_schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'trans_name': {
        'type': 'string',
    },
    'IMDB_socre': {
        'type': 'string',
    },
    'resolution': {
        'type': 'string',
    },
    'actors': {
        'type': 'string',
    },
    'name': {
        'type': 'string',
    },
    'language': {
        'type': 'string',
    },
    'screenshot': {
        'type': 'string',
    },
    'level': {
        'type': 'string',
    },
    'dytt8_url': {
        'type': 'string',
    },
    'duration': {
        'type': 'string',
    },
    'ftpurl': {
        'type': 'string',
    },
    'subtitles': {
        'type': 'string',
    },
    'director': {
        'type': 'string',
    },
    'format': {
        'type': 'string',
    },
    'conutry': {
        'type': 'string',
    },
    'decade': {
        'type': 'string',
    },
    'publish': {
        'type': 'string',
    },
    'type': {
        'type': 'string',
    },
    'size': {
        'type': 'string',
    },
    'placard': {
        'type': 'string',
    },
    'douban_score': {
        'type': 'string',
    },
}

people = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'person',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'lastname'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': schema
}

lastest_moive = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'moive',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    # 'additional_lookup': {
    #     'url': 'regex("[\w]+")',
    #     'field': 'lastname'
    # },

    # We choose to override global cache-control directives for this resource.
    # 'cache_control': 'max-age=10,must-revalidate',
    # 'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET'],
    'item_methods': ['GET'],

    'schema': moive_schema
}

DOMAIN = {
    'people': people,
    'lastest_moive': lastest_moive,
}
