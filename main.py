from pymongo import MongoClient
from fastapi import FastAPI, APIRouter, HTTPException
from Models.models import Algorithm,algorithms_dict
from database.configurations import collection
from Models.schemas import all_algorithms
from bson import ObjectId

app = FastAPI()
router = APIRouter()


@router.get("/")
async def root():
    return {"message": "hello to algoretmia, your website to learn and train algorithms"}


@router.post("/algorithm")
async def create_algo(new_algo:Algorithm):
    try:                

        complexityType = algorithms_dict.get(new_algo.complexity)

        if complexityType is None:
           raise ValueError(f"complexity '{new_algo.complexity} is not defined")
       
        response = collection.insert_one({
            "name": new_algo.name,
            "description": new_algo.description,
            "complexity": complexityType,
            "is_done": new_algo.is_done,
            "creation": new_algo.creation
        })
      
        return {"status_code": 201, "id": str(response.inserted_id)}

    except Exception as e:
        return HTTPException(status_code=500, detail=f"{e}")


@router.get("/algorithms")
async def show_algos():
    algos = collection.find()

    return all_algorithms(algos)




@router.get("/algorithms/algorithm/{algo_id}")
async def show_algo(algo_id: str):
    try:
        id = ObjectId(algo_id)
        
        print(id)
        
        algo = collection.find_one({"_id": id})
        
        if algo is None:
            raise HTTPException(status_code=404, detail="algorithm not found")
        
        # Convert ObjectId to string for JSON serialization
        algo["_id"] = str(algo["_id"])
        
        return {"status_code": 200, "algorithm": algo}
        
    except Exception as e:
        return HTTPException(status_code=500,detail=f"some error occurred {e}")

app.include_router(router)
# if __name__ == "__main__":
#     main()
