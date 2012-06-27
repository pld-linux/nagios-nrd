# TODO
# - subpackages for client/server
%include	/usr/lib/rpm/macros.perl
Summary:	Nagios Result Distributor (NSCA protocol redefined)
Name:		nagios-nrd
Version:	0.1
Release:	0.1
License:	GPL v3
Group:		Networking
Source0:	nrd.tar.xz
# Source0-md5:	71d3d4b105283cc1e7e3ab5d83e6a1e2
URL:		https://code.google.com/p/nrd/
BuildRequires:	perl-Module-Install
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nsca2

%prep
%setup -q -n nrd

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/NRD/Daemon/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nrd
%attr(755,root,root) %{_bindir}/send_nrd
%dir %{perl_vendorlib}/NRD
%{perl_vendorlib}/NRD/Client.pm
%{perl_vendorlib}/NRD/Daemon.pm
%{perl_vendorlib}/NRD/Packet.pm
%{perl_vendorlib}/NRD/Serialize.pm
%dir %{perl_vendorlib}/NRD/Serialize
%{perl_vendorlib}/NRD/Serialize/crypt.pm
%{perl_vendorlib}/NRD/Serialize/digest.pm
%{perl_vendorlib}/NRD/Serialize/plain.pm
%{perl_vendorlib}/NRD/Writer.pm
%dir %{perl_vendorlib}/NRD/Writer
%{perl_vendorlib}/NRD/Writer/cmdfile.pm
%{perl_vendorlib}/NRD/Writer/resultdir.pm
%{_mandir}/man3/NRD::Client.3pm*
%{_mandir}/man3/NRD::Daemon.3pm*
%{_mandir}/man3/NRD::Packet.3pm*
%{_mandir}/man3/NRD::Serialize.3pm*
%{_mandir}/man3/NRD::Writer.3pm*
