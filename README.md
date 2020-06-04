# WhatNow :computer: :heavy_check_mark:
Web application for managing tasks of different software projects.

## Requirements
You need to install the requirements.

```pip install -r requirements.txt```

## Explanation
WhatNow provides different functionality for the users.
For now, they are:
* Developer
* Team leader
* Project manager

### Registrtion
By default, everyone registers like a developer, and the admin can change the user's type as a project manager.
In turn, the project manager can choose a developer to be a team leader.

### Permissions
Developer:
* Can see their tasks which are 'in progress', in 'review' or 'done'.
* Can change the status of a task (without review and closing it).
* Can review other tasks.

Team leader:
* Can distribute developers who will work for a given task.
* Can review tasks.
* Can close a task.

Project manager:
* Can create a project.
* Can choose a team leader.
* Can add new tasks for a project.

**Everyone can writes comments.**

### Profile
Every user has a profile page. There they can upload a picture, write a bio, and add more information about them.