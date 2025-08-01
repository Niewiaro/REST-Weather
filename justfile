# ============================================
# Justfile – Development automation for Django + Docker
# ============================================

# Use PowerShell on Windows as the default shell
set shell := ["powershell", "-NoProfile", "-Command"]

# Alternatively, for Unix/bash environments:
# set shell := ["bash", "-cu"]

# 🧪 Run Django tests inside the Docker container
test:
    docker compose run --rm django-web python manage.py test

# 🔍 Check for missing migrations without making any changes
check-migrations:
    docker compose run --rm django-web python manage.py makemigrations --check --dry-run

# ✅ Apply all migrations
migrate:
    docker compose run --rm django-web python manage.py migrate

# 🔎 Run Django's built-in system checks
check:
    docker compose run --rm django-web python manage.py check

# 🎨 Check Python code formatting using Black
lint:
    pip install black
    black . --check --diff

# ✅ Run all project validations in sequence (formatting, migrations, system check, tests)
verify:
    just lint
    just check-migrations
    just check
    just test

# 🚀 Start all services after running full project validation
up: verify
    docker compose up --build

# 🚀 Start services only (skip tests and checks)
up-only:
    docker compose up --build

# 🛑 Stop and remove all Docker containers and volumes
down:
    docker compose down -v

# 🔧 Rebuild the Django Docker image only
build:
    docker compose build django-web

# 🐚 Open a shell session inside the Django container
shell:
    docker compose exec django-web bash

# 📁 Collect static files to /static_root
collectstatic:
    docker compose exec django-web python manage.py collectstatic --noinput

# 📜 Tail logs from the Django container
logs:
    docker compose logs -f django-web
