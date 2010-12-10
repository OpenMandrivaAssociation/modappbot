%define name	modappbot
%define version 0.4.6
%define release %mkrel 7

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
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%{__cp} -a etc-exemples %{buildroot}%{_sysconfdir}/modappbot

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc BUGS CHANGEMENTS LISEZMOI UPGRADE TODO
%{_bindir}/modappbot
%config(noreplace) %{_sysconfdir}/modappbot

