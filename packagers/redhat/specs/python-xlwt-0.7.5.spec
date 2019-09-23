Summary:		A library to create Microsoft Excel (tm) spreadsheet files
Name:			python-xlwt
Version:		0.7.5
Release:		1%{?dist}
License:		GPLv2
URL:			https://github.com/python-excel/xlwt
Source0:		https://codeload.github.com/python-excel/xlwt/tar.gz/xlwt-%{version}.tar.gz
Group:			Development/Languages
BuildArch:		noarch
BuildRequires:		python-devel


%description
Xlwt is a library for generating spreadsheet files that are compatible with
Excel 97/2000/XP/2003, OpenOffice.org Calc, and Gnumeric. xlwt has full support
for Unicode. Excel spreadsheets can be generated on any platform without
needing Excel or a COM server. The only requirement is Python 2.3 to 2.6.
xlwt is a fork of pyExcelerator.

It may be recommended to to install python-xlrd along with this package for
reading Excel spreadsheets.

%prep
%setup -q -n xlwt-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitelib}/xlwt
%{python_sitelib}/xlwt-%{version}-py2.*.egg-info

%changelog
* Tue Jul 23 2013 Sergio Tocalini Joerg <sergiotocalini@gmail.com> - 0.7.5
- Initial spec with python-xlwt-0.7.5 version.
