Summary:	SuckMT, a multithreaded suck replacement
Summary(pl.UTF-8):   SuckMT - wielowątkowy zamiennik sucka
Name:		suckmt
Version:	0.55
Release:	1
License:	GPL
Group:		Applications/News
Source0:	http://oss.basjes.nl/SuckMT/Files/%{name}-%{version}.tar.gz
# Source0-md5:	7306deaef3f0c4ef9ff5c65070b1547a
Source1:	%{name}-scripts.tar.gz
# Source1-md5:	7355887f92e953171b903253c4c004e1
Patch0:		%{name}-ac.patch
URL:		http://oss.basjes.nl/SuckMT/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
Provides:	news-sucker
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains software to download news from an NNTP server to
your local machine. This software was inspired by suck
(http://home.att.net/~bobyetman/) but has a major difference with
suck: SuckMT will open several NNTP connections simultaneously to
reduce the required connect time. To upload new messages back to the
NNTP server you will still need tools from the suck package.

%description -l pl.UTF-8
SuckMT to program do ściągania newsów z serwera NNTP na twój lokalny
komputer. Inspiracją był program suck, od którego SuckMT dość wyraźnie
się odróżnia: SuckMT otwiera kilka równoległych połączeń z serwerem
NNTP aby ograniczyć czas połączenia. Aby przesłać artykuły z powrotem
do serwera NNTP potrzebujesz narzędzi z pakietu suck.

%prep
%setup -q
%patch0 -p1

%build
%{__make} configure
%configure
%{__make} \
	COMPILER_DEBUG="%{rpmcflags} -DSUCK_CONFIG_FILE=\\\"%{_sysconfdir}/suckmt/suckmt.ini\\\""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_var}/lib/suckmt
tar zx -f %{SOURCE1} -C $RPM_BUILD_ROOT%{_var}/lib/suckmt

%{__make} rpminstall \
	DESTDIR=$RPM_BUILD_ROOT \
	configdir=%{_sysconfdir}/suckmt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README ChangeLog suckmt.ini.sample AUTHORS NEWS
%attr(755,root,root) %{_bindir}/suckmt
%attr(750,news,news) %dir %{_sysconfdir}/suckmt
%config(noreplace,missingok) %verify(not md5 mtime size) %attr(660,news,news) %{_sysconfdir}/suckmt/suckmt.ini
%attr(750,news,news) %dir %{_var}/spool/suckmt
%attr(750,news,news) %dir %{_var}/spool/suckmt/in.coming
%attr(750,news,news) %dir %{_var}/lib/suckmt
%attr(750,news,news) %{_var}/lib/suckmt/*
