### Booking Management

Service Booking Management

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app https://github.com/Maddy0102/Service-Booking-Management.git --branch develop
bench install-app booking_management
```

### Documentation
https://docs.google.com/document/d/104DrK4B5L4CtTzGUaTWIJDC_6u3vXPUc82nuXBgybzc/edit?usp=sharing

### System Info

○ OS (Ubuntu 22.04)
○ Python version --- Python 3.10.12
○ ERPNext/Frappe version -- erpnext 15.65.4 / frappe 15.71.0
○ Editors used (VS Code)


### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit
