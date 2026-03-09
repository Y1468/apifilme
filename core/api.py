from ninja import NinjaAPI
from filmes.api import filme_router
from filmes.apifilme import api_filme

api=NinjaAPI()
api.add_router('',filme_router)
api.add_router('',api_filme)