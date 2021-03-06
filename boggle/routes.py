import logging

from aiohttp import web

from boggle.resources import games, gamewords

logger = logging.getLogger(__name__)


def init(app: web.Application) -> None:
    app.router.add_get('/games', games.get)
    app.router.add_post('/games', games.post)
    app.router.add_put('/games/{game_id}', games.put)
    app.router.add_post('/games/{game_id}/words', gamewords.post)
    logger.info('Initialized routes')
