![](https://img.shields.io/github/issues/certmichelin/PTART.svg)
![](https://img.shields.io/github/forks/certmichelin/PTART.svg)
![](https://img.shields.io/github/stars/certmichelin/PTART.svg)
![](https://img.shields.io/github/license/certmichelin/PTART.svg)

# PTART (PenTests, Audits, and Reporting Tool).

PTART is a vulnerability organizer tool developed for pentesters, bug bounty hunters, anybody who wants to leverage its security expertise. Basically this tool will help you to :

- Report a vulnerabiltity with screenshots, attachments, CVSSv3.1 Score, CVSSv4.0 Score, OWASP top 10 labels in less than 3min.
- Facilitate reviewing with hit lifecycle.
- Avoid retyping again and again the same vulnerabilities content by using templates (common and personal).
- Generate attack scenarios that can be imagined using your findings.
- Generate ToDo lists from pentest methodologies (OWASP and Wahh are natively included) and assign tasks to a project member.
- Generate automatically a nice HTML/PDF RevealJS report.
- Generate automatically an Excel report to share status with your management.
- Generate automatically a full report in LaTeX.
- Plan retest campaigns based upon your initial project.
- Customize yours labels for categorizing vulnerabilities.
- Have discussions on a bug using the comment area.
- Have a common and shared workspace within the team.
- Secure your work with 2FA.
- Use PTART API with dedicated token for 3rd party application.
- Prepare the Burp configuration file according to project scope.
- Ask Chat GPT to write your report ;-)

A special thanks to [@pavanw3b](https://twitter.com/pavanw3b) for the [Sh00t!](https://github.com/pavanw3b/sh00t) project.

## Glossary

- **Flag:** It's a test case that needs to be tested. Flags can be generated automatically based on the testing methodology chosen or directly during the pentest. Based on our experience, flags are often useful when we are busy to struggle with an endpoint and we see a new point of interest in order to come back to it afterward.

- **Hit:** Hits are **bugs**. Typically a hit contains technical description of the bug, Affected Files/URLs, Steps To Reproduce and Fix Recommendation. Screenshots, attachments, comments can enrich the content of the vulnerability.

- **Assessment:** Assessment is a testing assessment. It can be an assessment of an application, a program - up to the user the way wanted to manage. It's a part of project.

- **Project:** Project contains assessments. Project can be a logical separation of what you do. It can be different job, bug bounty, up to you to decide.

## Screenshots

### PTART main page

![enter image description here](https://raw.githubusercontent.com/certmichelin/PTART/master/docs/3.PNG)

### Create a new hit

![enter image description here](https://raw.githubusercontent.com/certmichelin/PTART/master/docs/1.PNG)

### Simply paste a screenshot to add it!

![enter image description here](https://raw.githubusercontent.com/certmichelin/PTART/master/docs/2.PNG)

### Automatic LaTeX report creation

![enter image description here](https://raw.githubusercontent.com/certmichelin/PTART/master/docs/12.PNG)
![enter image description here](https://raw.githubusercontent.com/certmichelin/PTART/master/docs/11.PNG)

### Automatic Excel report creation

![enter image description here](https://raw.githubusercontent.com/certmichelin/PTART/master/docs/13.PNG)

### Automatic HTML report creation

![enter image description here](https://raw.githubusercontent.com/certmichelin/PTART/master/docs/5.PNG)
![enter image description here](https://raw.githubusercontent.com/certmichelin/PTART/master/docs/6.PNG)

### Comments in your presentation

![enter image description here](https://raw.githubusercontent.com/certmichelin/PTART/master/docs/8.PNG)

### Asset management

![enter image description here](https://raw.githubusercontent.com/certmichelin/PTART/master/docs/9.PNG)

### Attack Scenario

![enter image description here](https://raw.githubusercontent.com/certmichelin/PTART/master/docs/10.PNG)

### Retest Campaign

![enter image description here](https://raw.githubusercontent.com/certmichelin/PTART/master/docs/14.png)
![enter image description here](https://raw.githubusercontent.com/certmichelin/PTART/master/docs/16.png)

### Syntax highlight

```java
// Your First Program
class HelloWorld {
   public static void main(String[] args) {
      System.out.println("Hello, World!");
   }
}
```

### Chat GPT

In order to enable, the `Chat GPT` console, you just need to enter your api key in settings.py upon `CHATGPT_API_KEY` key.

![enter image description here](https://raw.githubusercontent.com/certmichelin/PTART/master/docs/15.png)

## Quick setup using Docker Compose

You could easily instatiate a demo version by using our docker version.

```bash
cp .env.template .env
docker compose up -d

# Init PTART.
docker compose exec ptart-server python manage.py migrate
docker compose exec ptart-server python manage.py createsuperuser
docker compose exec ptart-server python loader_cwes_4.17.py 
docker compose exec ptart-server python loader_owasp_testing_guide.py
```

Access [http://localhost:8000/](http://localhost:8000/) on your favorite browser !!

## How to DEV

### Quick setup with docker compose

The environment includes:

- Django (with auto-reload)
- PostgreSQL
- All required system dependencies (Pandoc, Cairo, etc.)

#### Prerequisites

- Docker ≥ 24
- Docker Compose ≥ v2

#### Start the dev environment

```bash
git clone https://github.com/certmichelin/PTART.git
cd PTART
cp .env.template .env
docker compose -f docker-compose.dev.yaml up --build -d
```

#### First time setup

```bash
docker compose -f docker-compose.dev.yaml exec ptart-server python manage.py migrate
docker compose -f docker-compose.dev.yaml exec ptart-server python manage.py createsuperuser

# Optional
docker compose -f docker-compose.dev.yaml exec ptart-server python loader_cwes_4.17.py
docker compose -f docker-compose.dev.yaml exec ptart-server python loader_owasp_testing_guide.py
```

#### Stop the environment

```bash
docker compose -f docker-compose.dev.yaml down
```

### Setup with local venv

Prerequisites

- Python 3.13
- PostgreSQL
- Pandoc 3.2.x
- System libraries (libpq, cairo, etc.)

### Project setup

```bash
git clone https://github.com/certmichelin/PTART.git
cd PTART/app
cp .env.template .env
```

Create a venv in `./app/.venv`

```bash
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r app/requirements.txt
```

Install pandoc : 

```bash
# Linux
# Get pandoc binary at https://github.com/jgm/pandoc/releases/latest
wget https://github.com/jgm/pandoc/releases/download/3.8.3/pandoc-3.8.3-1-amd64.deb -O /tmp/pandoc.deb
sudo dpkg -i /tmp/pandoc.deb

# MacOS
brew install pandoc

# Windows
choco install pandoc
# OR
# Get pandoc binary at https://github.com/jgm/pandoc/releases/latest
```

#### Database Setup

```bash
docker run -d --name ptart_db \
  -e POSTGRES_USER=ptart \
  -e POSTGRES_PASSWORD=ptart \
  -e POSTGRES_DB=ptart \
  -p 5432:5432 postgres:15
```

Or you can use your own external postgres database by changing values in `.env` file. Then, setup the tables and create the admin user : 

```bash
python manage.py migrate
python manage.py createsuperuser

# Optional
python loader_cwes_4.17.py
python loader_owasp_testing_guide.py
```

#### Starting PTART

```bash
python manage.py runserver
```

Then, you can access PTART at `http://127.0.0.1:8000` on your favorite web browser.

### Upgrading PTART

1. Pull the latest code base via git: `git pull` or download the source from Github and replace the files.
2. Navigate to the app folder.
3. Stop the server if it's running: `Ctrl + C`
4. Setup any additional dependencies: `pip install -r requirements.txt`
5. Make the latest database changes: `python manage.py migrate`
6. Start the server: `python manage.py runserver`
7. Enjoy
