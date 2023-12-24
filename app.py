from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__, static_url_path='/static')

shortlisted_array = []
# designers_data = []
sorlisted_click = []
design_data = [{
  "id": 1,
  'name': 'Epic Designs',
  'rating': 4,
  'description':
  'Passionate team of 4 designers working out <br> of Bangalore with an experience of 8 years.',
  'projects': 57,
  'experience': 8,
  'price': '$$$',
  'tel1': '+91 - 984532853',
  'tel2': '+91 - 984532854'
}, {
  "id": 2,
  'name': 'Studio - D3',
  'rating': 3,
  'description':
  'Passionate team of 4 designers working out <br> of Bangalore with an experience of 6 years.',
  'projects': '43',
  'experience': 6,
  'price': '$$',
  'tel1': '+91 - 984532874',
  'tel2': '+91 - 984532876'
}, {
  "id": 3,
  'name': 'House of designs',
  'rating': 3,
  'description':
  'Passionate team of 4 designers working out <br> of Bangalore with an experience of 3 years.',
  'projects': 40,
  'experience': 3,
  'price': '$$$',
  'tel1': '+91 - 984532812',
  'tel2': '+91 - 984532821'
}, {
  "id": 4,
  'name': 'Royal Designs',
  'rating': 4,
  'description':
  'Passionate team of 4 designers working out <br> of Bangalore with an experience of 2 years.',
  'projects': 20,
  'experience': 2,
  'price': '$$$$',
  'tel1': '+91 - 984532832',
  'tel2': '+91 - 984532898'
}, {
  "id": 5,
  'name': 'Luxe Interiors',
  'rating': 3,
  'description':
  'Passionate team of 4 designers working out <br> of Bangalore with an experience of 4 years.',
  'projects': 60,
  'experience': 4,
  'price': '$$$',
  'tel1': '+91 - 984532809',
  'tel2': '+91 - 984532818'
}]

num_rectangles = len(design_data)
colors = ['#FFFCF2' if i % 2 == 0 else '#FFF' for i in range(num_rectangles)]

@app.route('/')
def index():


  return render_template('index.html',
                         num_rectangles=num_rectangles,
                         colors=colors,
                         design_data=design_data,
                         shortlisted_array=shortlisted_array)


@app.route('/add', methods=['POST'])
def update_tasks():
  try:
    # Get the JSON data from the request
    data = request.get_json()
    print("hai", data)

    # Update the todo_list with the received data
    shortlisted_array.append(data['tasks'])
    # arr=shortlisted_array[-1]
    print(shortlisted_array, "shortlisted_array")

    return jsonify({
        "status": "success",
        "message": "Tasks updated successfully"
    })
  except Exception as e:
    return jsonify({"status": "error", "message": str(e)})

@app.route('/delete', methods=['DELETE'])
def delete_task():
  try:
      # Get the JSON data from the request
      data = request.get_json()

      # Find and remove the task from the shortlisted_array
      task_to_delete = data.get('tasks')
      if task_to_delete in shortlisted_array:
          shortlisted_array.remove(task_to_delete)
          print(shortlisted_array, "shortlisted_array after deletion")

          return jsonify({
              "status": "success",
              "message": "Task deleted successfully"
          })
      else:
          return jsonify({
              "status": "error",
              "message": "Task not found in the shortlist"
          })

  except Exception as e:
      return jsonify({"status": "error", "message": str(e)})
# arr=shortlisted_array[-1]
@app.route('/sortlisted', methods=['GET'])
def get_tasks():
  return jsonify({"status": "success", "tasks": shortlisted_array})

@app.route('/shortl',methods=['GET', 'POST'])
def shortl():
  seen_ids = set()
  unique_list = []

  for dictionary in shortlisted_array:
      current_id = dictionary['id']
      if current_id not in seen_ids:
          unique_list.append(dictionary)
          seen_ids.add(current_id)

  print(unique_list,"uniquelist")
  print(shortlisted_array, "shortlisted_array")
  return render_template('shortlist.html', unique_list=unique_list,colors=colors,num_rectangles=num_rectangles)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
