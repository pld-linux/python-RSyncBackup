
%include	/usr/lib/rpm/macros.python
%define 	module RSyncBackup

Summary:	Python module for perform automatic backups using the rsync command
Summary(pl):	Modu� Pythona umo�liwiaj�cy wykonywanie automatycznych archiwizacji przy pomocy komendy rsync
Name:		python-%{module}
Version:	1.2
Release:	1
License:	BSD-like
Group:		Libraries/Python
Source0:	http://www.owlfish.com/software/utils/RSyncBackup/downloads/%{module}-%{version}.tar.gz
# Source0-md5:	a929fa15adcd6847f137599127c84280
URL:		http://www.owlfish.com/software/utils/RSyncBackup/
BuildRequires:	python-devel >= 2.3
Requires:	python >= 2.3
Requires:	rsync
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RSyncBackup is the Python module that allows automatic backups using
the rsync command. rsync has many different uses but is particularly
suitable for performng backups from one form of online storage to
another, either over a network or on a local machine with multiple
drives.

%description -l pl
RSyncBackup jest modu�em Pythona pozwalaj�cym na wykonywanie
automatycznych archiwizacji. rsync posiada wprawdzie wiele innych
mo�liwo�ci, ale szczeg�lnie u�yteczny jest do przeprowadzania
archiwizacji mi�dzy wieloma urz�dzeniami, zar�wno poprzez sie� jak i
na lokalnej maszynie mi�dzy r�nymi dyskami.

%package doc
Summary:	Documentation for RSyncBackup module
Summary(pl):	Dokumentacja do modu�u RSyncBackup
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation files for RSyncBackup Python module.

%description doc -l p
Pakiet zawieraj�cy dokumentacj� dla modu�u Python RSyncBackup.

%package examples
Summary:	Examples for RSyncBackup module
Summary(pl):	Przyk�ady do modu�u RSyncBackup
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example files for RSyncBackup Python module.

%description doc -l p
Pakiet zawieraj�cy przyk�adowe skrypty dla modu�u Python RSyncBackup.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{_examplesdir}/%{name}-%{version}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitescriptdir} \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt LICENSE.txt
%{py_sitescriptdir}/RSyncBackup.py[oc]

%files doc
%defattr(644,root,root,755)
%doc documentation/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
