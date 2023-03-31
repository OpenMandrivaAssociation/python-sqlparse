%define pypi_name sqlparse

Name:           python-sqlparse
Version:        0.4.3
Release:        2
Group:          Development/Python
Summary:        Non-validating SQL parser

License:        BSD
URL:            https://github.com/andialbrecht/sqlparse
Source0:        https://pypi.python.org/packages/source/s/sqlparse/sqlparse-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-sphinx
BuildRequires:  python-sphinx_rtd_theme

%description
sqlparse is a non-validating SQL parser module.
It provides support for parsing, splitting and
formatting SQL statements.

%{?python_provide:%python_provide python-%{pypi_name}}
Provides:       %{pypi_name} = %{version}-%{release}

%prep
%setup -q -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

# generate html docs
PYTHONDIR=$(pwd) sphinx-build docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py_install

%files -n python-%{pypi_name}
%doc html README.rst
%{_bindir}/sqlformat
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py*.egg-info
