from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)

# Enable CORs for all origins to give unrestricted access.
CORS(app, origins="*")

@app.route('/', methods=['GET'])    #This decorator pretty much says: When someone visits the / URL, run this home()
def home():
    """Simple health check"""
    return jsonify({
        "status": "running",
        "message": "Webhook server is live!",
        "endpoints": ["/webhook"]
    })

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    current_date = datetime.now().isoformat()
    
    print(f"Webhook called at {current_date}") 
    #Those print statements will actually be printed on the Railway Deploy logs.
    if request.method == 'POST' and request.json:
        print(f"Received data: {request.json}")
    
    response_data = {
        "list_of_ingredients": 'cherry tomatoes, lime, pepper, mixed greens, chicken apple sausage, olive oil',
        "estimated_foodmass": "645.8g",
        "calories": "354.0 kcal",
        "fat": "48.1 g",
        "carbs": "8.5g",
        "protein": "43.4g",
        "inference_time": "3.48s",
        "date": current_date
    }

    return jsonify(response_data)




def web():
    current_date = datetime.now().isoformat()


if __name__ == '__main__':
    # Railway provides PORT environment variable
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
