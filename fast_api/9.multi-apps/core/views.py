import os
import importlib.util

from fastapi import FastAPI

app = FastAPI()

def load_apps():
    apps = os.listdir('apps')
    
    for x in apps:
        view_path = os.path.join('apps', x, 'views.py')
        if not os.path.exists(view_path):
            continue

        spec = importlib.util.spec_from_file_location(f"apps.{x}.views", view_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        app.include_router(module.router, prefix=f"/{x}")

@app.get('/')
async def main():
    return {'message':'Hello'}

load_apps()