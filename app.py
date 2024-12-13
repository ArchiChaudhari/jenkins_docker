from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for tasks
tasks = [
    {"id": 1, "title": "Learn Docker", "completed": False},
    {"id": 2, "title": "Build a Python app", "completed": True},
]

# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

# Get a single task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task)

# Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    if not data or "title" not in data:
        return jsonify({"error": "Invalid input"}), 400
    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "completed": False,
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# Update a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    data = request.json
    if "title" in data:
        task["title"] = data["title"]
    if "completed" in data:
        task["completed"] = data["completed"]
    return jsonify(task)

# Delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Task deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
