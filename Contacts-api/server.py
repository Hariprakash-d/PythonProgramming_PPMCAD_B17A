from flask import Flask,request, jsonify

app = Flask(__name__)

contacts = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
]

next_id = 4

@app.route('/hello')
def hello_route():
    print("Hello, World!, We are learning Flask!")
    return "Hello, World!, We are learning Flask!"

@app.get('/contacts')   # Decorator to define a route for GET requests to '/contacts'
def list_contacts():
    return contacts

@app.get('/contacts/<contact_id>')  # Decorator to define a route for GET requests to '/contacts/<contact_id>'
def get_contact(contact_id):
    # contact = next((c for c in contacts if c["id"] == contact_id), None)
    # if contact:
    #     return contact
    # else:
    #     return {"error": "Contact not found"}, 404
    for contact in contacts:
        if contact["id"] == int(contact_id):
            return contact

    return {"error": "Contact not found"}, 404

@app.post('/contacts')  # Decorator to define a route for POST requests to '/contacts'
def create_contact():
    global next_id
    new_contact = {
        "id": f'{next_id}',
        "name": request.json["name"],
        "email": request.json["email"]
    }
    contacts.append(new_contact)
    next_id += 1
    return new_contact, 201

@app.put('/contacts/<contact_id>')  # Decorator to define a route for PUT requests to '/contacts/<contact_id>'
def update_contact(contact_id):
    for contact in contacts:
        if contact["id"] == int(contact_id):
            contact["name"] = request.json.get("name", contact["name"]) if "name" in request.json else contact["name"]
            contact["email"] = request.json.get("email", contact["email"]) if "email" in request.json else contact["email"]
            return contact

    return {"error": "Contact not found"}, 404

@app.delete('/contacts/<contact_id>')  # Decorator to define a route for DELETE requests to '/contacts/<contact_id>'
def delete_contact(contact_id):
    for contact in contacts:
        if contact["id"] == int(contact_id):
            contacts.remove(contact)
            return {"message": "Contact deleted", "contact": contact}

    return {"error": "Contact not found"}, 404

app.run(debug=True, host='127.0.0.1', port=5000)
