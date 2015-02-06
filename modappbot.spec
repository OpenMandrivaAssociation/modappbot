%define name	modappbot
%define version 0.4.6
%define release 9

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A robot written in perl to moderate Usenet groups
Summary(fr):	Robot-modérateur écrit en Perl pour modérer des groupes de discussion Usenet
License:	Artistic
Group:		Networking/News
Url:		http://www.frmug.org/usenet/mod/
Source:		http://www.frmug.org/usenet/mod/%{name}-%{version}.tar.bz2
Patch:		modappbot.patch
BuildArch:	noarch

%description
A robot written in perl to moderate Usenet groups

%description -l fr
Robot-modérateur écrit en Perl pour modérer des groupes de discussion 
Usenet

%prep
%setup -q
%patch

%install
%{__mkdir} -p %{buildroot}/%{_bindir} %{buildroot}%{_sysconfdir}
%{__install} -m 755 modappbot %{buildroot}%{_bindir}
cp -pr etc-exemples %{buildroot}%{_sysconfdir}/modappbot

%clean

%files
%defattr(-,root,root)
%doc BUGS CHANGEMENTS LISEZMOI UPGRADE TODO
%{_bindir}/modappbot
%config(noreplace) %{_sysconfdir}/modappbot



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.6-7mdv2011.0
+ Revision: 620387
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.4.6-6mdv2010.0
+ Revision: 430084
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.4.6-5mdv2009.0
+ Revision: 241029
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sat Apr 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.6-3mdk
- spec cleanup
- drop useless exception
- drop useless explicit requires
- %%mkrel

* Mon Apr 10 2006 Bruno Cornec <bcornec@mandrake.org> 0.4.6-2mdk
- Rebuilt at robot request

* Wed Mar 23 2005 Bruno Cornec <bcornec@mandrake.org> 0.4.6-1mdk
- First package made

