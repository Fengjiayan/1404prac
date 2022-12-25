"""
project
Estimate: 100 minutes
Actual:   82 minutes
"""
import datetime
from project import Project


def main():
    """Main function."""
    filename = "projects.txt"
    projects = load_projects(filename)
    while True:
        select = get_menu_select()
        if select == "L":
            projects = load_projects(filename)
            print("Successfully loaded data.")
        elif select == "S":
            save_projects(projects, filename)
            print("Successfully save data.")
        elif select == "D":
            display_projects(projects)
        elif select == "F":
            filter_projects(projects)
        elif select == "A":
            add_project(projects)
        elif select == "U":
            update_project(projects)
        else:
            print("Thank you for using custom-built project management software.")
            break


def get_menu_select():
    """Get user select from menu."""
    while True:
        print_menu()
        select = input(">>> ").upper()
        if select not in ["L", "S", "D", "F", "A", "U", "Q"]:
            print("Invalid Option!")
        else:
            return select


def print_menu():
    """Print main menu."""
    print("""- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit""")


def load_projects(filename):
    """Load projects from file."""
    projects = []
    # Open the file for reading
    in_file = open(filename, "r")
    in_file.readline()
    for line in in_file:
        # Strip newline from end and split it into parts
        parts = line.strip().split('\t')
        project = create_project(parts)
        projects.append(project)
    # Close the file as soon as we've finished reading it
    in_file.close()
    return projects


def save_projects(projects, filename):
    """Save projects to file."""
    out_file = open(filename, "w")
    # Open the file for writing
    title = ["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"]
    out_file.write("\t".join(title) + "\n")
    if projects is not None:
        for project in projects:
            data = [project.name, project.start_date.strftime("%d/%m/%Y"),
                    str(project.priority), str(project.cost_estimate), str(project.completion_percentage)]
            out_file.write("\t".join(data) + "\n")
    # Close the file as soon as we've finished writing it
    out_file.close()
    return projects


def display_projects(projects):
    """Display projects."""
    if projects is None:
        return
    incomplete_projects = []
    completed_projects = []
    for project in sorted(projects):
        if project.is_complete():
            completed_projects.append(project)
        else:
            incomplete_projects.append(project)
    """Display incomplete projects."""
    if incomplete_projects:
        print("Incomplete projects:")
        for project in incomplete_projects:
            print("  " + str(project))
    """Display completed projects."""
    if completed_projects:
        print("Completed projects:")
        for project in completed_projects:
            print("  " + str(project))


def filter_projects(projects):
    """Display filter projects."""
    if projects is None:
        return
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    result = [project for project in projects if project.start_date >= date]
    for project in sorted(result, key=lambda p: p.start_date):
        print(project)


def add_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion_percentage = input("Percent complete: ")
    project = create_project([name, start_date, priority, cost_estimate, completion_percentage])
    projects.append(project)


def update_project(projects):
    """Update a project."""
    if projects is None:
        return
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_index = int(input("Project choice: "))
    if project_index < 0 or project_index >= len(projects):
        return
    project = projects[project_index]
    print(project)
    new_percentage = input("New Percentage: ").strip()
    new_priority = input("New Priority: ").strip()
    if new_percentage != "":
        project.completion_percentage = int(new_percentage)
    if new_priority != "":
        project.priority = int(new_priority)


def create_project(parts):
    """Create a project from attribute list."""
    name = parts[0]
    start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
    priority = int(parts[2])
    cost_estimate = float(parts[3])
    completion_percentage = int(parts[4])
    return Project(name, start_date, priority, cost_estimate, completion_percentage)



main()
