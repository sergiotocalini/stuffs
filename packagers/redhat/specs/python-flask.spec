Summary:		Flask: A microframework based on Werkzeug, Jinja2 and good intentions
Name:			python-flask
Version:		0.10.1
Release:		1%{?dist}
License:		GPLv2
URL:			http://flask.pocoo.org/
Source0:		http://pypi.python.org/packages/source/F/Flask/Flask-%{version}.tar.gz
Group:			Development/Languages
BuildArch:		noarch
BuildRequires:		python-devel
Requires:		python-babel
Requires:		python-itsdangerous
Requires:		python-jinja2
Requires:		python-markupsafe
Requires:		python-werkzeug

%description
Flask is a microframework for Python based on Werkzeug and Jinja2. It's intended for getting started very quickly and was developed with best intentions in mind.

%prep
%setup -q -n Flask-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitelib}/flask
%{python_sitelib}/Flask-%{version}-py2.*.egg-info

%changelog
* Fri Jul 5 2014 Sergio Tocalini Joerg <sergiotocalini@gmail.com> - 0.10.1-r1
- Initial spec with python-flask-0.10.1 version.
