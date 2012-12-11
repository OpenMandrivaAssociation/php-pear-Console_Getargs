%define		_class		Console
%define		_subclass	Getargs
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.3.5
Release:	%mkrel 3
Summary:	A command-line arguments parser
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Console_Getargs/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The Console_Getargs package implements a Command Line arguments parser
that your CLI applications can use to parse arguments found in
\$_SERVER['argv']. It performs some basic arguments validation and is
capable to return a formatted help text to the user, based on the
configuration it is given.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{upstream_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.5-3mdv2012.0
+ Revision: 741828
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.5-2
+ Revision: 679267
- mass rebuild

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.5-1mdv2011.0
+ Revision: 587638
- update to new version 1.3.5

* Sun Dec 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.4-5mdv2010.1
+ Revision: 478292
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.3.4-4mdv2010.0
+ Revision: 440948
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-3mdv2009.1
+ Revision: 321913
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-2mdv2009.0
+ Revision: 236809
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-1mdv2008.0
+ Revision: 15642
- 1.3.4


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-1mdv2007.0
+ Revision: 81409
- Import php-pear-Console_Getargs

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-1mdk
- 1.3.1

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-5mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-4mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-3mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-2mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-1mdk
- 1.3.0

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-1mdk
- initial Mandriva package (PLD import)

