import copy

# Define a project with tasks and sub-tasks
project_data = {
    "project_name": "Website Development",
    "tasks": [
        {
            "task_name": "Design",
            "sub_tasks": ["Create mockups", "Gather feedback", "Finalize design"]
        },
        {
            "task_name": "Development",
            "sub_tasks": ["Set up environment", "Implement features", "Fix bugs"]
        }
    ]
}

# Create a shallow copy of the project data
shallow_copy = copy.copy(project_data)

# Create a deep copy of the project data
deep_copy = copy.deepcopy(project_data)

# Modify the shallow copy
shallow_copy["tasks"][0]["sub_tasks"].append("Review design")
shallow_copy["tasks"].append({"task_name": "Testing", "sub_tasks": []})

# Modify the deep copy
deep_copy["tasks"][1]["sub_tasks"].append("Deployment")
deep_copy["tasks"][1]["sub_tasks"].remove("Fix bugs")

# Print the original project data
print("Original Project Data:")
print(project_data)

# Print the shallow copy
print("\nShallow Copy:")
print(shallow_copy)

# Print the deep copy
print("\nDeep Copy:")
print(deep_copy)
 
