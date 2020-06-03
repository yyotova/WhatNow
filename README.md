# WhatNow :computer: :heavy_check_mark:
Web application for managing tasks of different software projects.

## Requirements
This is a Django app.So, you need to install it first.
```python -m pip install Django```

## Explanation
WhatNow provides different functionality for the users.
For now, they are:
* Developer
* Team leader
* Project manager

### Registrtion
By default, everyone registers like developer and the admin can change the user's type.

### Permissions
* Developers can olny see their tasks which are 'in progress', in 'review' or 'done'.
* Team leaders can add which developers will work for a given task.
* Project managers can add new tasks for a project.

