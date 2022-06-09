from fastapi import FastAPI 

api = FastAPI(title="Mon API pour la promo MAI22_BCDE")

@api.get("/welcome")
def welc():
    """
    Cette route est pour souhaiter la bienvenue à tous
    """
    return {"data":"Welcome to all"}
    
@api.get("/number")
def number():
    """
    Cette route retourne un nombre 
    """
    return 1