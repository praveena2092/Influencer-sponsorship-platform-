# Influencer Engagement & Sponsorship Coordination Platform

A Flask web app that connects brands (sponsors) with influencers, manages
influencer-marketing campaigns, and tracks ad requests between the two sides.
Built as the **MAD-1 (Modern Application Development I)** project for the
IIT Madras BS Degree program.

## Features

| Role | Capabilities |
|------|--------------|
| **Admin** | Sign up / log in, view sponsors, influencers, campaigns and ad requests |
| **Sponsor** | Sign up / log in, update or delete profile, create / update / delete campaigns, create / update / delete ad requests, search and view influencers |
| **Influencer** | Sign up / log in, update or delete profile, search and view campaigns, view ad requests, accept or reject them |

## Tech stack

- **Flask** – web framework
- **Flask-SQLAlchemy** – ORM
- **Flask-RESTful** – REST endpoints
- **SQLite** – database (created automatically on first run)
- **Jinja2 + Bootstrap** – front end

## Getting started

Requires Python 3.9+.

```bash
git clone https://github.com/<your-username>/influencer-sponsorship-platform.git
cd influencer-sponsorship-platform

# Option A: one-step helper
./run.sh

# Option B: manual
python -m venv env
source env/bin/activate        # Windows: env\Scripts\activate
pip install -r requirements.txt
python main.py
```

The app starts on <http://localhost:5000>. The SQLite database is created in
`instance/` the first time it runs.

## Project structure

```
.
├── main.py                      # App factory and entry point
├── application/
│   ├── config.py                # Configuration
│   ├── database.py              # SQLAlchemy instance
│   ├── models.py                # Admin, Sponsors, Influencers, Campaign, Ad_request
│   ├── admin_controller.py      # Admin routes
│   ├── sponsor_controller.py    # Sponsor routes
│   ├── influencer_controller.py # Influencer routes
│   └── rest*.py                 # REST API resources
├── templates/                   # Jinja2 templates
├── static/                      # CSS and images
└── docs/
    ├── project-report.pdf       # Project report
    └── demo-video.mp4           # Demo walkthrough
```

## Data model

- **Admin** – id, name, password
- **Sponsors** – name, industry, budget, password; one-to-many with Campaign
- **Influencers** – name, category, niche, reach, password
- **Campaign** – belongs to a sponsor; name, description, dates, budget, visibility, goals
- **Ad_request** – links sponsor, influencer and campaign; message, requirements, payment amount, status

## Known limitations

This is a course project and not production-ready:

- Passwords are stored and compared in plain text (no hashing).
- There is no session handling or authentication on routes.
- No production configuration is set up (`ENV=production` raises an error).

## Author

Praveena N (22f3001454) – IIT Madras BS Degree

## License

[MIT](LICENSE)
