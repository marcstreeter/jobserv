from setuptools import setup

requires = [
    "Werkzeug>=0.14.1",
    "flask>=1.0.2",
    "Flask-SQLAlchemy>=2.3.2",
    "Flask-Migrate>=2.3.1",
    "Flask-Testing>=0.7.1",
    "google_cloud_storage>=1.13.2",
    "gunicorn>=19.9.0",
    "PyYAML>=4.2b4",
    "requests>=2.21.0",
    "PyMySQL>=0.9.3",
    "wheel>=0.32.3",
    "pykwalify>=1.7.0",
    "python-dateutil>=2.7.5",
    "pytz>=2018.7",
    "setproctitle>=1.1.10",
    "cryptography>=2.4.2",
    "bcrypt>=3.1.5",
    "pyjwt>=1.7.1",
    "dataclasses>=0.6.0",
]

setup(
    name="jobserv",
    version="0.1.0",
    description="jobserv library",
    author="foundries.io",
    url="https://github.com/foundriesio/jobserv",
    packages=["jobserv"],
    python_requires="~=3.6",
    install_requires=requires,
)