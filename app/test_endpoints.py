import requests
import sys

BASE_URL = "http://127.0.0.1:8003"

def test_create_item():
    """Test creating a new item"""
    try:
        data = {
            "name": "Test Item",
            "description": "This is a test item",
            "price": 29.99
        }
        
        response = requests.post(f"{BASE_URL}/items/", json=data)
        print("\nCreate Item Response:", response.status_code)
        print(response.json())
        return response.json()["id"]
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to the server. Make sure FastAPI is running on port 8001")
        sys.exit(1)
    except Exception as e:
        print(f"Error during create item: {str(e)}")
        sys.exit(1)

def test_get_all_items():
    """Test getting all items"""
    try:
        response = requests.get(f"{BASE_URL}/items/")
        print("\nGet All Items Response:", response.status_code)
        print(response.json())
    except Exception as e:
        print(f"Error during get all items: {str(e)}")

def test_get_item(item_id):
    """Test getting a specific item"""
    try:
        response = requests.get(f"{BASE_URL}/items/{item_id}")
        print("\nGet Specific Item Response:", response.status_code)
        print(response.json())
    except Exception as e:
        print(f"Error during get item: {str(e)}")

def test_update_item(item_id):
    """Test updating an item"""
    try:
        data = {
            "name": "Updated Test Item",
            "description": "This is an updated test item",
            "price": 39.99
        }
        
        response = requests.put(f"{BASE_URL}/items/{item_id}", json=data)
        print("\nUpdate Item Response:", response.status_code)
        print(response.json())
    except Exception as e:
        print(f"Error during update item: {str(e)}")

def test_delete_item(item_id):
    """Test deleting an item"""
    try:
        response = requests.delete(f"{BASE_URL}/items/{item_id}")
        print("\nDelete Item Response:", response.status_code)
        print(response.json())
    except Exception as e:
        print(f"Error during delete item: {str(e)}")

if __name__ == "__main__":
    print("Starting API Tests...")
    try:
        # Create and get ID of test item
        item_id = test_create_item()
        
        # Test other endpoints
        test_get_all_items()
        test_get_item(item_id)
        test_update_item(item_id)
        test_delete_item(item_id)
        
        print("\nAll tests completed!")
    except Exception as e:
        print(f"\nTest failed: {str(e)}")