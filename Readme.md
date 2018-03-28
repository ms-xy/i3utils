### i3utils

Small python3 helper program leveraging i3-msg to allow renaming workspaces
and moving to (number+colon prefixed) workspaces.

# Example:

To switch to the workspace that is either named "2" or "2:something" use:

```bash
i3utils switch 2
```

To set the title of the current workspace use:

```bash
i3utils title "2: my special workspace with a title"
```
