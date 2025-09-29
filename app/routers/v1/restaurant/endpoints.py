from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.configs.database import get_db
from app.services.restaurant_service import RestaurantService
from .schemas import RestaurantCreate, RestaurantUpdate, RestaurantResponse, AllergenResponse, RestaurantMenuResponse

router = APIRouter()


@router.get("/", response_model=List[RestaurantResponse])
async def get_restaurants(db: AsyncSession = Depends(get_db)):
    """Get all active restaurants."""
    service = RestaurantService(db)
    restaurants = await service.get_all_restaurants()
    return restaurants


@router.get("/{restaurant_id}", response_model=RestaurantResponse)
async def get_restaurant(restaurant_id: int, db: AsyncSession = Depends(get_db)):
    """Get a restaurant by ID."""
    service = RestaurantService(db)
    restaurant = await service.get_restaurant_by_id(restaurant_id)
    
    if not restaurant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Restaurant not found"
        )
    
    return restaurant


@router.post("/", response_model=RestaurantResponse, status_code=status.HTTP_201_CREATED)
async def create_restaurant(
    restaurant_data: RestaurantCreate, 
    db: AsyncSession = Depends(get_db)
):
    """Create a new restaurant."""
    service = RestaurantService(db)
    restaurant = await service.create_restaurant(restaurant_data.model_dump())
    return restaurant


@router.put("/{restaurant_id}", response_model=RestaurantResponse)
async def update_restaurant(
    restaurant_id: int,
    restaurant_data: RestaurantUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Update a restaurant."""
    service = RestaurantService(db)
    restaurant = await service.update_restaurant(restaurant_id, restaurant_data.model_dump(exclude_unset=True))
    
    if not restaurant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Restaurant not found"
        )
    
    return restaurant


@router.delete("/{restaurant_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_restaurant(restaurant_id: int, db: AsyncSession = Depends(get_db)):
    """Soft delete a restaurant."""
    service = RestaurantService(db)
    success = await service.delete_restaurant(restaurant_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Restaurant not found"
        )
    
    return None


@router.get("/{restaurant_id}/allergens", response_model=List[AllergenResponse])
async def get_restaurant_allergens(restaurant_id: int, db: AsyncSession = Depends(get_db)):
    """Get all allergens associated with a restaurant's menu items."""
    service = RestaurantService(db)
    
    # Check if restaurant exists
    restaurant = await service.get_restaurant_by_id(restaurant_id)
    if not restaurant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Restaurant not found"
        )
    
    allergens = await service.get_restaurant_allergens(restaurant_id)
    return allergens


@router.get("/{restaurant_id}/menu", response_model=RestaurantMenuResponse)
async def get_restaurant_menu(restaurant_id: int, db: AsyncSession = Depends(get_db)):
    """Get restaurant menu organized by categories."""
    service = RestaurantService(db)
    
    # Check if restaurant exists
    restaurant = await service.get_restaurant_by_id(restaurant_id)
    if not restaurant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Restaurant not found"
        )
    
    menu = await service.get_restaurant_menu(restaurant_id)
    return menu