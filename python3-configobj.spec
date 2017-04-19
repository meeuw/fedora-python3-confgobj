%if 0%{?python3_pkgversion}
%global python3_pkgversion 34
%endif

%global with_python3 1
%global pypi_name configobj

Name:           python3-%{pypi_name}
Version:        5.0.6
Release:        8%{?dist}
Summary:        Config file reading, writing, and validation

Group:          System Environment/Libraries
License:        BSD
URL:            http://configobj.readthedocs.org/
# Moved to the github release instead of the pypi one since multiple elements (License and tests)
# are not available using pypi. Two bugs have been filled about this:
# https://github.com/DiffSK/configobj/issues/98
# https://github.com/DiffSK/configobj/issues/99
# Source0:        https://pypi.python.org/packages/source/c/configobj/configobj-5.0.6.tar.gz
Source0:        https://github.com/DiffSK/%{pypi_name}/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-pytest

%description
ConfigObj is a simple but powerful configuration file reader and writer: an ini
file round tripper. Its main feature is that it is very easy to use, with a
straightforward programmer's interface and a simple syntax for config files. 

%package -n python%{python3_pkgversion}-configobj
Summary:        Config file reading, writing, and validation for Python 3

Requires:       python%{python3_pkgversion}-six
%description -n python%{python3_pkgversion}-configobj
ConfigObj is a simple but powerful configuration file reader and writer: an ini
file round tripper. Its main feature is that it is very easy to use, with a
straightforward programmer's interface and a simple syntax for config files. 

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
# this needs to be set for tests.test_configobj.test_options_deprecation
export PYTHONWARNINGS=always
%{__python3} test_configobj.py
py.test-%{python3_version} tests

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/*
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Sun Mar 12 2017 Dick Marinus <dick@mrns.nl> - 5.0.6-8
initial version
