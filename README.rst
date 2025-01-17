aiolog
======
Asynchronous handlers for standard python logging library.
Currently telegram (requires ``aiohttp``)
and smtp (via ``aiosmtplib``) handlers are available.


Installation
------------
::

    pip install aiolog

Repository: https://github.com/imbolc/aiolog


Configuration
-------------
Just use any way you prefer to configure built-in ``logging`` library, e.g.:

.. code-block:: python

    logging.config.dictConfig({
        'version': 1,
        'handlers': {
            'telegram': {
                # any built-in `logging.Handler` params
                'level': 'DEBUG',
                'class': 'aiolog.telegram.Handler',

                # common `aiolog` params
                'timeout': 10,  # 60 by default
                'queue_size': 100,  # 1000 by default

                # handler specific params
                'token': 'your telegram bot token',
                # feature to send logs for multiplie chats
                'chats': 'admin_chat_id_1, admin_chat_id_2, ...',
            },
            'smtp': {
                'level': 'WARNING',
                'class': 'aiolog.smtp.Handler',
                'hostname': 'smtp.yandex.com',
                'port': 465,
                'sender': 'bot@email',
                'recipient': 'your@email',
                'use_tls': True,
                'username': 'smtp username',
                'password': 'smtp password',
            },
        },
        'loggers': {
            '': {
                'handlers': [
                    'telegram',
                    'smtp',
                ],
                'level': 'DEBUG',
            },
        }
    })


Usage
-----
You can use built-in ``logging`` library as usual,
just add starting and stopping of ``aiolog``.

.. code-block:: python

    log = logging.getLogger(__name__)

    async def hello():
        log.debug('Hey')

    aiolog.start()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello())
    loop.run_until_complete(aiolog.stop())


Look at the ``example`` folder for more examples.


aiohttp
^^^^^^^
With ``aiohttp``, you can use a little more sugar.
Instead of starting and stopping ``aiolog`` directly, you can use:

.. code-block:: python

    aiolog.setup_aiohttp(app)
