Summary:		Python module for generating and verifying JSON Web Tokens.
Name:			python-jwt
Version:		9999
Release:		1%{?dist}
License:		GPLv2
URL:			https://github.com/davedoesdev/python-jwt
Source0:		https://github.com/davedoesdev/python-jwt/archive/python-jwt-master.zip
Group:			Development/Languages
BuildArch:		noarch
BuildRequires:		python-devel


%description
Module for generating and verifying JSON Web Tokens.
Uses python-jws to do the heavy lifting.
Supports RS256, RS384, RS512, PS256, PS384, PS512, HS256, HS384, HS512 and none signature algorithms.
Unit tests, including tests for interoperability with node-jsjws.

%prep
%setup -q -n python-jwt-master

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitelib}/jwt
%{python_sitelib}/jwt-%{version}-py2.*.egg-info

%changelog
* Fri Jul 18 2014 Sergio Tocalini Joerg <sergiotocalini@gmail.com> - 9999-1
- Initial spec with python-jwt-9999 version.
