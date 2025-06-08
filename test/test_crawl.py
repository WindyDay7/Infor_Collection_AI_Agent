from config import settings

print(settings.SERPAPI_KEY)
print(settings.MODELS)
open_router_models = settings.MODELS.get("open_router_models", []).split(',')
ali_mota_models = settings.MODELS.get("ali_mota_models", []).split(',')

print("open_router_models: ", open_router_models)
print("ali_mota_models: ", ali_mota_models)