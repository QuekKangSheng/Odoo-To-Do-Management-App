# Odoo Todo List Management Module

A custom Odoo 17 module for internal todo list management, built as part of a Software Developer Internship technical assessment.

---

## About

This module allows internal users to create and manage todo lists with structured items, attendees, tags, and status tracking. It is built on the Odoo 17 framework using Python and XML, and is designed for productivity and task management within an organisation.

### Requirements
- Docker Desktop
- Git
- Odoo 17 (via Docker)
- PostgreSQL 15 (via Docker)

---

## Features

- Create todo lists with a title, tags, start date and end date
- Validate that end date is always later than start date
- Track progress across three stages — Draft, In Progress, Complete
- Add todo items directly in the list without opening a popup (inline editing)
- Mark individual items as finished — checkbox only visible when In Progress
- "Mark as Complete" button appears automatically only when all items are checked
- Assign attendees linked to existing Odoo users
- All fields become read-only when status is Complete
- Filter dropdown with Uncomplete (Draft + In Progress) and Complete options
- Default view of the list would show all tasks regardless of status
- Default tags pre-loaded on install — Work, Event, Life Achievement (more can be added)

---

## Module Structure
```
todo_list/
├── __init__.py
├── __manifest__.py
├── data/
│   └── tags_data.xml          # Default tags
├── models/
│   └── todo_list.py           # All models
├── security/
│   └── ir.model.access.csv    # CRUD permissions
└── views/
    ├── menu.xml                # App menus
    └── todo_list_views.xml     # List, form and search views
```

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/QuekKangSheng/Odoo-To-Do-Management-App.git 
cd Odoo-To-Do-Management-App
```

### 2. Start the containers
```bash
docker-compose up -d
```

### 3. Open Odoo in your browser
```
http://localhost:8069
```

### 4. Create a database
Fill in the setup form with your preferred credentials:
- **Database Name:** e.g. `odoo_todo`
- **Email:** your email address
- **Password:** your chosen password
- Leave Demo Data unticked
- Click Create Database
```

### 5. Enable Developer Mode
Settings → scroll to bottom → Activate Developer Mode

### 6. Install/Activate the module
Apps → Update Apps List → search **Todo List** → Activate

---

## Test Results

All 10 requirements from the assessment have been tested and verified.

| # | Test | Result |
|---|------|--------|
| 1 | Title field is required — blocks save when empty | ✅ Pass |
| 2 | End date must be later than start date — shows validation error | ✅ Pass |
| 3 | Default tags (Work, Event, Life Achievement) loaded on install | ✅ Pass |
| 4 | Status defaults to Draft on new record | ✅ Pass |
| 5 | Start button transitions status from Draft to In Progress | ✅ Pass |
| 6 | Finished checkbox only visible when status is In Progress | ✅ Pass |
| 7 | Todo items support inline editing without popup | ✅ Pass |
| 8 | Mark as Complete button only appears when all items are checked | ✅ Pass |
| 9 | All fields become read-only when status is Complete | ✅ Pass |
| 10 | Filter dropdown correctly filters Uncomplete (Draft + In Progress) and Complete records | ✅ Pass |
| 11 | Default view of the list would display all tasks regardless of status | ✅ Pass |

---

## Branching Strategy

| Branch | Purpose |
|--------|---------|
| `main` | Production-ready code — final submission state |
| `develop` | Active development and testing |

All development and testing is done on `develop`. Code is merged into `main` via Pull Request only when fully tested and working.

---

## Odoo 17 Compatibility Notes

- Views use `<tree>` tag instead of the old `<list>` tag
- Conditional visibility uses inline expressions e.g. `invisible="status != 'draft'"` instead of the deprecated `attrs=` syntax
- Fields used in `invisible=` expressions must be declared in the view even if hidden e.g. `all_items_done`

---

## Author

Built by Quek Kang Sheng as part of the Software Developer Internship Exercise/Assessment.
```
