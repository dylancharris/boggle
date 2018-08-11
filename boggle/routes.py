import logging

from aiohttp import web

from boggle.resources import games

logger = logging.getLogger(__name__)


def init(app: web.Application) -> None:
    app.router.add_get('/games', games.get)
    app.router.add_post('/games', games.post)
    logger.info('Initialized routes')
