#!/usr/bin/python3


"""
A script to fetch and display the TODO list progress for a given employee
using a REST API.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):

    """
    Fetch and display the TODO list progress for a given employee.

    Args:
    employee_id (int): The ID of the employee.

    Returns:
    None
    """
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user information
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)

    # Check if the user request was successful
    if user_response.status_code != 200:
        print("Error fetching user data")
        return

    # Parse the user JSON data
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch TODO list for the user
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)

    # Check if the TODO list request was successful
    if todos_response.status_code != 200:
        print("Error fetching TODO list data")
        return

    # Parse the TODO list JSON data
    todos_data = todos_response.json()

    # Calculate the number of completed and total tasks
    total_tasks = len(todos_data)
    done_tasks = [todo for todo in todos_data if todo.get('completed')]
    number_of_done_tasks = len(done_tasks)

    # Print the result in the specified format
    print(f"Employee {employee_name} is done with tasks(
        {number_of_done_tasks}/{total_tasks}):")

    # Print the title of completed tasks with proper indentation
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    # Ensure the script is called with exactly one argument
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        # Convert the argument to an integer (employee ID)
        employee_id = int(sys.argv[1])
        # Fetch and display the employee's TODO list progress
        get_employee_todo_progress(employee_id)
    except ValueError:
        # Handle the case where the provided employee ID is not an integer
        print("Employee ID must be an integer")
        sys.exit(1)
