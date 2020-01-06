%define pypi_name sqlparse

Name:           python-sqlparse
Version:        0.3.0
Release:        %mkrel 3
Group:          Development/Python
Summary:        Non-validating SQL parser

License:        BSD
URL:            https://github.com/andialbrecht/sqlparse
Source0:        https://pypi.python.org/packages/source/s/sqlparse/sqlparse-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description
sqlparse is a non-validating SQL parser module.
It provides support for parsing, splitting and
formatting SQL statements.

%package -n     python3-%{pypi_name}
Summary:        Non-validating SQL parser
Group:          Development/Python
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       %{pypi_name} = %{version}-%{release}
Conflicts:      python2-%{pypi_name} < 0.3.0
Conflicts:      python-%{pypi_name} < 0.3.0

%description -n python3-%{pypi_name}
sqlparse is a non-validating SQL parser module.
It provides support for parsing, splitting and
formatting SQL statements.

%prep
%setup -q -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

# generate html docs
PYTHONDIR=$(pwd) sphinx-build docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%files -n python3-%{pypi_name}
%doc html README.rst
%{_bindir}/sqlformat
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
