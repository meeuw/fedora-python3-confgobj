%global upname configobj
%global checkout 20131004hg10adc6e7d759
%global shortc 10adc6e7d759

Name: python3-configobj
Version: 4.7.2
Release: 5.%{checkout}%{?dist}
Summary: Config file reading, writing, and validation
License: BSD

URL: https://bitbucket.org/pkumar/configobj-py3
Source0: https://bitbucket.org/pkumar/configobj-py3/get/%{shortc}.tar.bz2
Patch0: configobj-import-all-fix.patch
BuildArch: noarch
# Asked to include LICENSE.txt
# https://bitbucket.org/pkumar/configobj-py3/pull-request/1/add-licensetxt/diff

BuildRequires: python3-devel

%description
ConfigObj is a simple but powerful config file reader and writer: an ini file
round tripper. Its main feature is that it is very easy to use, with a
straightforward programmer's interface and a simple syntax for config files. 
It has lots of other features though:
    * Nested sections (subsections), to any level
    * List values
    * Multiple line values
    * String interpolation (substitution)
    * Integrated with a powerful validation system
          o including automatic type checking/conversion
          o repeated sections
          o and allowing default values
    * All comments in the file are preserved
    * The order of keys/sections is preserved
    * No external dependencies
    * Full Unicode support
    * A powerful unrepr mode for storing basic datatypes

%prep
%setup -qn pkumar-configobj-py3-%{shortc}
%patch0 -p1 -b .all

%build
%{__python3} setup.py build 

%install
%{__python3} setup.py install --skip-build --root %{buildroot}

%check
export PYTHONPATH="%{buildroot}/%{python3_sitelib}"
%{__python3} -m unittest functionaltests.test_configobj functionaltests.test_validate_errors
 
%files
%doc docs/*.html docs/*.txt docs/*.css
%{python3_sitelib}/*

%changelog
* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 4.7.2-5.20131004hg10adc6e7d759
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Oct 06 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 4.7.2-4.20131004hg10adc6e7d759
- Reverting to previous upstream
- Asked to add LICENSE file

* Sat Oct 05 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 4.7.2-3.20131005hg75b2805d35b9
- Switched upstream URL to a fork
- Include LICENSE.txt

* Fri Oct 04 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 4.7.2-2.20131004hg10adc6e7d759
- Fix traceback when doing from validate import * (pacth from python-configobj)

* Thu Oct 03 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 4.7.2-1.20131004hg10adc6e7d759
- Initial spec
