Summary:	SuckMT, a multithreaded suck replacement
Name:		suckmt
Version:	0.41
Release:	1
Source:		http://www.wirehub.nl/~basjesn/Files/%{name}-%{version}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root
License:	GPL
Group:		News
Provides:	news-sucker

%description
This package contains software to download news from an NNTP server to your
local machine. This software was inspired by suck
(http://home.att.net/~bobyetman/) but has a major difference with suck:
SuckMT will open several NNTP connections  simultaneously to reduce the
required connect time. To upload new messages back to the NNTP server you
will still need tools from the suck package.

%prep
%setup -q
%build
aclocal
autoconf
automake
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf INSTALL README ChangeLog suckmt.ini.sample

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {INSTALL,README,ChangeLog,suckmt.ini.sample}.gz
%attr(755,root,root) %{_bindir}/suckmt
