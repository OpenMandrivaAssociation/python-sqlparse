%define module sqlparse

Name:		python-sqlparse
Version:	0.5.5
Release:	1
Group:		Development/Python
Summary:	A non-validating SQL parser module for Python
License:	BSD-3-Clause
URL:		https://github.com/andialbrecht/sqlparse
Source0:	https://pypi.python.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(sphinx)
BuildRequires:	python%{pyver}dist(sphinx-rtd-theme)
BuildRequires:	python%{pyver}dist(wheel)
%{?python_provide:%python_provide python-%{module}}
Provides:	%{module} = %{version}-%{release}

%description
%{name} is a non-validating SQL parser module.
It provides support for parsing, splitting and
formatting SQL statements.

%prep
%autosetup -n %{module}-%{version} -p1
sed -i -e '1{\,^#!%{_bindir}/env python,d}' sqlparse/__main__.py sqlparse/cli.py
chmod -x sqlparse/cli.py

%build
%py_build
# generate html docs
PYTHONDIR=$(pwd) sphinx-build docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%files
%doc html README.rst
%{_bindir}/sqlformat
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
