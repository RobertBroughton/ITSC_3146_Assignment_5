from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .models import models, schemas
from .controllers import orders
from .controllers import sandwiches
from .controllers import resources
from .controllers import recipes
from .controllers import order_details
from .dependencies.database import engine, get_db
from .models.models import Sandwich, Resource

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Orders-API Enpoints
@app.post("/orders/", response_model=schemas.Order, tags=["Orders"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=order)


@app.get("/orders/", response_model=list[schemas.Order], tags=["Orders"])
def read_orders(db: Session = Depends(get_db)):
    return orders.read_all(db)


@app.get("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def update_one_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = orders.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.update(db=db, order=order, order_id=order_id)


@app.delete("/orders/{order_id}", tags=["Orders"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, order_id=order_id)

#Sandwichs-API Endpoints
@app.post("/sandwiches/", response_model=schemas.Sandwich, tags=["Sandwiches"])
def create_sandwich(sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    return sandwiches.create(db=db, sandwich=sandwich)

@app.get("/sandwiches/", response_model=list[schemas.Sandwich], tags=["sandwiches"])
def read_sandwichs(db: Session = Depends(get_db)):
    return sandwiches.read_all(db)

@app.get("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["sandwiches"])
def read_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = sandwiches.read_one(db, sandwich_id=sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sandwich

@app.put("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["sandwiches"])
def update_one_sandwich(sandwich_id: int, sandwich: schemas.SandwichUpdate, db: Session = Depends(get_db)):
    sandwich_db = sandwiches.read_one(db, sandwich_id=sandwich_id)
    if sandwich_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sandwiches.update(db=db, sandwich=sandwich, sandwich_id=sandwich_id)

@app.delete("/sandwiches/{sandwich_id}", tags=["sandwiches"])
def delete_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = sandwiches.read_one(db, sandwich_id=sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sandwiches.delete(db=db, sandwich_id=sandwich_id)
#Resources-API Endpoints
@app.post("/resources/", response_model=schemas.Resource, tags=["resources"])
def create_resource(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return resources.create(db=db, resource=resource)

@app.get("/resources/", response_model=list[schemas.Resource], tags=["resources"])
def read_resources(db: Session = Depends(get_db)):
    return resources.read_all(db)

@app.get("/resources/{resource_id}", response_model=schemas.Resource, tags=["resources"])
def read_one_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = resources.read_one(db, resource_id=resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resource

@app.put("/resources/{resource_id}", response_model=schemas.Resource, tags=["resources"])
def update_one_resource(resource_id: int, resource: schemas.ResourceUpdate, db: Session = Depends(get_db)):
    resource_db = resources.read_one(db, resource_id=resource_id)
    if resource_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resource.update(db=db, resource=resource, resource_id=resource_id)

@app.delete("/resource/{resource_id}", tags=["resources"])
def delete_one_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = resources.read_one(db, resource_id=resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resources.delete(db=db, resource_id=resource_id)

#Recipes-API Endpoints
@app.post("/Recipes/", response_model=schemas.Recipe, tags=["Recipes"])
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipes.create(db=db, recipes=recipe)

@app.get("/Recipes/", response_model=list[schemas.Recipe], tags=["Recipes"])
def read_recipes(db: Session = Depends(get_db)):
    return recipes.read_all(db)

@app.get("/Recipes/{Recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
def read_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = recipes.read_one(db, recipe_id=recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipe

@app.put("/Recipes/{Recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
def update_one_recipe(recipe_id: int, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    recipe_db = recipes.read_one(db, recipe_id=recipe_id)
    if recipe_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipes.update(db=db, recipe=recipe, recipe_id=recipe_id)

@app.delete("/Recipes/{Recipe_id}", tags=["Recipes"])
def delete_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = recipes.read_one(db, recipe_id=recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipes.delete(db=db, recipe_id=recipe_id)

#OrderDetail-API Endpoints
@app.post("/OrderDetail/", response_model=schemas.OrderDetail, tags=["OrderDetail"])
def create_order_detail(order_detail: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    return order_details.create(db=db, order_details=order_detail)

@app.get("/OrderDetail/", response_model=list[schemas.OrderDetail], tags=["OrderDetail"])
def read_order_details(db: Session = Depends(get_db)):
    return order_details.read_all(db)

@app.get("/OrderDetail/{order_detail_id}", response_model=schemas.OrderDetail, tags=["OrderDetail"])
def read_one_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    order_detail = order_details.read_one(db, order_detail_id=order_detail_id)
    if order_detail is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order_detail

@app.put("/OrderDetail/{order_detail_id}", response_model=schemas.OrderDetail, tags=["OrderDetail"])
def update_one_order_detail(order_detail_id: int, order_detail: schemas.OrderDetailUpdate, db: Session = Depends(get_db)):
    order_detail_db = order_details.read_one(db, order_detail_id=order_detail_id)
    if order_detail_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order_details.update(db=db, order_detail=order_detail, order_detail_id=order_detail_id)

@app.delete("/OrderDetail/{order_detail_id}", tags=["OrderDetail"])
def delete_one_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    order_detail = order_details.read_one(db, order_detail_id=order_detail_id)
    if order_detail is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order_details.delete(db=db, order_detail_id=order_detail_id)