%define		dbname	City
Summary:	GeoLite2 City - City database for GeoIP
Summary(pl.UTF-8):	GeoLite2 City - baza danych miast dla GeoIP
Name:		GeoLite2-db-%{dbname}
# Updated every month:
Version:	20131210
Release:	1
License:	CC 3.0 BY-SA
Group:		Applications/Databases
Source0:	http://geolite.maxmind.com/download/geoip/database/GeoLite2-%{dbname}.mmdb.gz?/GeoLite2-%{dbname}-%{version}.mmdb.gz
# Source0-md5:	ca142991d3594c8b65faa45ac442e1f3
URL:		http://dev.maxmind.com/geoip/geoip2/geolite2/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GeoLite2 databases are free IP geolocation databases comparable to,
but less accurate than, MaxMind's GeoIP2 databases.

GeoLite2 databases are updated on the first Tuesday of each month.

%prep
%setup -qcT
cp -p %{SOURCE0} GeoLite2-%{dbname}.mmdb.gz

gunzip GeoLite2-%{dbname}.mmdb.gz

ver=$(TZ=GMT stat -c '%y' GeoLite2-%{dbname}.mmdb | awk '{print $1}' | tr -d -)
if [ "$ver" != %{version} ]; then
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/GeoIP
cp -p GeoLite2-%{dbname}.mmdb $RPM_BUILD_ROOT%{_datadir}/GeoIP

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/GeoIP/*.mmdb
